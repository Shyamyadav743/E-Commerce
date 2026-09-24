# E-Commerce Sales Analytics & Customer Intelligence — Project Report

## 1. Project Overview

This project is an end-to-end e-commerce sales analytics and customer intelligence workflow. It is designed to load transaction data, prepare it for analysis, calculate business KPIs, segment customers using RFM analysis, build revenue forecasting models, and export visualizations.

## 2. Objectives

- Clean and prepare e-commerce transaction data.
- Calculate revenue, order, unit, discount, and customer KPIs.
- Analyze revenue by product category and sales trends over time.
- Segment customers using Recency, Frequency, and Monetary (RFM) scoring.
- Compare Linear Regression and Gradient Boosting for sequential monthly revenue modeling.
- Export reusable charts for reporting and presentation.
- Provide reproducible project documentation and dependency information.

## 3. Technology Stack

- Python 3
- pandas — data loading, transformation, aggregation
- NumPy — numerical operations
- Matplotlib — visualization
- Seaborn — plot styling
- scikit-learn — machine-learning models and metrics
- ReportLab — available for PDF/report generation workflows

## 4. Project Files

| File | Purpose |
|---|---|
| `eda_sales_analysis.py` | Main analytics, RFM, forecasting, and visualization code |
| `requirements.txt` | Python dependencies |
| `README.md` | Project overview, setup, usage, and repository structure |
| `PROJECT_REPORT.md` | This detailed project report |

The current repository also expects the transaction dataset `ecommerce_sales_data_500.csv` when the analysis script is executed. That dataset is not currently stored in the repository tree.

## 5. Data Preparation

The Python workflow:

1. Reads the transaction CSV with pandas.
2. Converts `Order_Date` to a datetime value.
3. Fills missing customer ratings with the dataset median.
4. Creates a `YearMonth` period field for monthly aggregation.

The expected dataset contains order/date and customer identifiers, category/product information, quantity, pricing/discount fields, sales totals, payment method, region, fulfillment status, and customer rating.

## 6. Key Performance Indicators

The implementation calculates:

- Total revenue
- Total orders
- Average order value (AOV)
- Total units sold
- Average discount percentage
- Unique customers

These KPIs provide a compact view of sales volume, customer reach, pricing/discount behavior, and order economics.

## 7. RFM Customer Segmentation

RFM analysis is performed at customer level:

- **Recency:** days since the customer's most recent order.
- **Frequency:** number of orders associated with the customer.
- **Monetary:** total sales attributed to the customer.

Each dimension is converted to a 1–5 score using quintiles. Recency scoring is reversed so that more recent customers receive higher scores.

The implemented segments are:

- Champions
- Loyal Customers
- Potential Loyalists
- At Risk
- Lost Customers

This segmentation can support retention, loyalty, and win-back analysis.

## 8. Revenue Forecasting

Monthly revenue is aggregated and assigned a sequential month number. Two models are fitted:

1. Linear Regression
2. Gradient Boosting Regressor

The implementation reports:

- Mean Absolute Error (MAE)
- R²
- A next-month revenue estimate from each fitted model

The current script evaluates predictions on the same monthly observations used for fitting. Therefore, these metrics describe in-sample fit rather than a held-out forecast evaluation. For production forecasting, a time-based train/test split or rolling validation should be added.

## 9. Visualizations

The script exports the following PNG charts to the selected output directory:

- `category_revenue.png`
- `monthly_sales_trend.png`
- `rfm_segments.png`
- `fulfillment_status.png`
- `payment_methods.png`

These charts cover category performance, monthly revenue, customer segmentation, fulfillment outcomes, and payment-method usage.

## 10. How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python eda_sales_analysis.py --data ecommerce_sales_data_500.csv --output plots
```

The dataset path can be changed with `--data`, and the visualization directory can be changed with `--output`.

## 11. Current Repository Verification

At the time this report was added, the repository contained:

- `eda_sales_analysis.py`
- `requirements.txt`
- `README.md`

A dedicated project report was missing, so this `PROJECT_REPORT.md` file has been added.

The transaction CSV and generated plot/report artifacts referenced by the README were not present in the repository tree during verification. They should be added if they are intended to be version-controlled and distributed with the project.

## 12. Recommended Next Steps

- Add the source transaction CSV if redistribution is permitted.
- Add generated plots after running the analysis.
- Add automated tests for KPI and RFM calculations.
- Use a time-based validation strategy for forecasting.
- Add a generated PDF report if a PDF submission is required.
- Consider adding a `LICENSE` and `.gitignore` for a complete public project repository.

## 13. Conclusion

The repository now has a documented analytics implementation, dependency specification, README, and dedicated project report. The Python script provides the core e-commerce analytics workflow, while the documentation explains the methodology, outputs, limitations, and reproducibility steps.
