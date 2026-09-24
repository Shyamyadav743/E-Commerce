# E-Commerce Sales Analytics & Customer Intelligence

An end-to-end data science project for e-commerce transaction analytics, customer RFM segmentation, sequential monthly revenue modeling, and visualization.

## Project scope

The project provides:

- CSV loading and preprocessing
- Executive sales KPIs
- Revenue and order analysis
- RFM customer segmentation
- Linear Regression and Gradient Boosting revenue modeling
- Exportable high-resolution charts
- Reproducible setup instructions
- A dedicated project report

## Repository structure

```text
.
├── README.md
├── PROJECT_REPORT.md
├── requirements.txt
└── eda_sales_analysis.py
```

### Expected input and generated outputs

The analysis script expects an input file named:

```text
ecommerce_sales_data_500.csv
```

When the script is run, it generates these charts inside `plots/`:

```text
plots/
├── category_revenue.png
├── monthly_sales_trend.png
├── rfm_segments.png
├── fulfillment_status.png
└── payment_methods.png
```

**Repository status:** the CSV dataset and generated `plots/` artifacts were not present when the repository was checked. They are therefore documented as expected inputs/outputs rather than listed as existing repository files.

## Main files

| File | Purpose |
|---|---|
| `eda_sales_analysis.py` | Main data preparation, KPI, RFM, forecasting, and plotting code |
| `requirements.txt` | Python package dependencies |
| `PROJECT_REPORT.md` | Detailed project methodology, limitations, and run instructions |
| `README.md` | Project overview and quick-start documentation |

## Dataset

The script is designed for an e-commerce transaction CSV containing fields such as:

- `Order_Date`
- `Order_ID`
- `Customer_ID`
- `Category`
- `Quantity`
- `Discount_Pct`
- `Total_Sales`
- `Payment_Method`
- `Order_Status`
- `Customer_Rating`

If your CSV uses a different schema, update the column references in `eda_sales_analysis.py` accordingly.

## Key Performance Indicators

The script calculates:

- Total revenue
- Total orders
- Average order value
- Total units
- Average discount percentage
- Unique customers

## RFM methodology

Recency, Frequency, and Monetary values are calculated for each customer. Each component receives a 1–5 quintile score.

The current segmentation rules produce:

- **Champions**
- **Loyal Customers**
- **Potential Loyalists**
- **At Risk**
- **Lost Customers**

## Forecasting

Monthly revenue is converted to a sequential month index and modeled with:

1. Linear Regression
2. Gradient Boosting Regressor

The script reports MAE, R², and a next-month estimate for each model.

**Important:** the current implementation evaluates predictions on the same observations used for fitting. The resulting metrics are therefore in-sample metrics, not a true held-out forecast score.

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python eda_sales_analysis.py --data ecommerce_sales_data_500.csv --output plots
```

After a successful run, inspect the generated PNG files in `plots/`.

## Requirements

The required Python packages are listed in `requirements.txt`:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- reportlab

## Project report

See [PROJECT_REPORT.md](PROJECT_REPORT.md) for the complete methodology, repository verification, limitations, and recommended next steps.
