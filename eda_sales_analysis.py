"""
E-Commerce Sales Analytics & Customer Intelligence
End-to-end preprocessing, KPI/EDA, RFM segmentation, ML forecasting, and plot export.
"""
import os
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score

plt.switch_backend("Agg")
sns.set_theme(style="whitegrid")

def load_and_prepare(data_path):
    df = pd.read_csv(data_path)
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="raise")
    df["Customer_Rating_Filled"] = df["Customer_Rating"].fillna(df["Customer_Rating"].median())
    df["YearMonth"] = df["Order_Date"].dt.to_period("M")
    return df

def compute_kpis(df):
    return {
        "total_revenue": float(df["Total_Sales"].sum()),
        "total_orders": int(len(df)),
        "aov": float(df["Total_Sales"].mean()),
        "total_units": int(df["Quantity"].sum()),
        "avg_discount_pct": float(df["Discount_Pct"].mean() * 100),
        "unique_customers": int(df["Customer_ID"].nunique()),
    }

def build_rfm(df):
    max_date = df["Order_Date"].max() + pd.Timedelta(days=1)
    rfm = df.groupby("Customer_ID").agg(
        Recency=("Order_Date", lambda x: (max_date - x.max()).days),
        Frequency=("Order_ID", "count"),
        Monetary=("Total_Sales", "sum"),
    ).reset_index()
    rfm["R_Score"] = pd.qcut(rfm["Recency"], 5, labels=[5,4,3,2,1]).astype(int)
    rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1,2,3,4,5]).astype(int)
    rfm["M_Score"] = pd.qcut(rfm["Monetary"], 5, labels=[1,2,3,4,5]).astype(int)

    def segment(row):
        r, f, m = row.R_Score, row.F_Score, row.M_Score
        if r >= 4 and f >= 4 and m >= 4:
            return "Champions"
        if r >= 3 and f >= 3:
            return "Loyal Customers"
        if r >= 3 and f < 3:
            return "Potential Loyalists"
        if r < 3 and f >= 3:
            return "At Risk"
        return "Lost Customers"

    rfm["Segment"] = rfm.apply(segment, axis=1)
    return rfm

def build_monthly(df):
    monthly = df.groupby("YearMonth", as_index=False).agg(
        Revenue=("Total_Sales", "sum"), Orders=("Order_ID", "count")
    )
    monthly["Month_Seq"] = np.arange(1, len(monthly) + 1)
    return monthly

def fit_forecasts(monthly):
    X, y = monthly[["Month_Seq"]], monthly["Revenue"]
    models = {
        "Linear Regression": LinearRegression(),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42, n_estimators=50),
    }
    metrics = {}
    for name, model in models.items():
        model.fit(X, y)
        pred = model.predict(X)
        metrics[name] = {
            "r2": float(r2_score(y, pred)),
            "mae": float(mean_absolute_error(y, pred)),
            "next_month": float(model.predict([[len(monthly)+1]])[0]),
        }
    return metrics

def save_plots(df, rfm, monthly, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    plt.figure(figsize=(9,5))
    cat = df.groupby("Category", as_index=False)["Total_Sales"].sum().sort_values("Total_Sales")
    plt.barh(cat["Category"], cat["Total_Sales"])
    plt.title("Revenue by Product Category (2024)")
    plt.xlabel("Revenue ($)"); plt.ylabel("")
    plt.tight_layout(); plt.savefig(os.path.join(out_dir,"category_revenue.png"), dpi=200); plt.close()

    plt.figure(figsize=(10,5))
    plt.plot(monthly["YearMonth"].astype(str), monthly["Revenue"], marker="o")
    plt.title("Monthly Sales Revenue Trend (2024)")
    plt.xlabel("Month"); plt.ylabel("Revenue ($)"); plt.xticks(rotation=45)
    plt.tight_layout(); plt.savefig(os.path.join(out_dir,"monthly_sales_trend.png"), dpi=200); plt.close()

    plt.figure(figsize=(8,5))
    seg = rfm["Segment"].value_counts().rename_axis("Segment").reset_index(name="Customer_Count")
    plt.barh(seg["Segment"], seg["Customer_Count"])
    plt.title("RFM Customer Segmentation")
    plt.xlabel("Customers"); plt.ylabel("")
    plt.tight_layout(); plt.savefig(os.path.join(out_dir,"rfm_segments.png"), dpi=200); plt.close()

    plt.figure(figsize=(8,5))
    status = df["Order_Status"].value_counts().rename_axis("Order_Status").reset_index(name="Orders")
    plt.barh(status["Order_Status"], status["Orders"])
    plt.title("Order Fulfillment Status")
    plt.xlabel("Orders"); plt.ylabel("")
    plt.tight_layout(); plt.savefig(os.path.join(out_dir,"fulfillment_status.png"), dpi=200); plt.close()

    plt.figure(figsize=(8,5))
    pay = df["Payment_Method"].value_counts().rename_axis("Payment_Method").reset_index(name="Orders")
    plt.barh(pay["Payment_Method"], pay["Orders"])
    plt.title("Orders by Payment Method")
    plt.xlabel("Orders"); plt.ylabel("")
    plt.tight_layout(); plt.savefig(os.path.join(out_dir,"payment_methods.png"), dpi=200); plt.close()

def run(data_path="ecommerce_sales_data_500.csv", output_dir="plots"):
    df = load_and_prepare(data_path)
    kpis = compute_kpis(df)
    rfm = build_rfm(df)
    monthly = build_monthly(df)
    metrics = fit_forecasts(monthly)
    save_plots(df, rfm, monthly, output_dir)
    print("\nKPI SUMMARY")
    for k,v in kpis.items(): print(f"{k}: {v}")
    print("\nRFM SEGMENTS")
    print(rfm["Segment"].value_counts())
    print("\nFORECAST METRICS")
    for k,v in metrics.items(): print(k, v)
    return df, kpis, rfm, monthly, metrics

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="ecommerce_sales_data_500.csv")
    p.add_argument("--output", default="plots")
    args = p.parse_args()
    run(args.data, args.output)
