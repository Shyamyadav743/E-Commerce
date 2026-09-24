# E-Commerce Sales Analytics & Customer Intelligence

An end-to-end data science portfolio project for transaction analytics, customer RFM segmentation, and sequential sales forecasting.

## Project scope

The master specification requires CSV loading/preprocessing, executive KPIs, RFM scoring into five customer segments, Linear Regression and Gradient Boosting forecasting, high-resolution plots, documentation, and a publication-quality PDF report.

## Dataset

`ecommerce_sales_data_500.csv` contains 500 transaction records covering 2024. The schema includes order/date/customer identifiers, category/product, quantity and unit price, discount, total sales, payment method, region, fulfillment status, and customer rating.

## Key results

- Total revenue: **$64,792.18**
- Orders: **500**
- AOV: **$129.58**
- Units sold: **810**
- Average discount: **4.83%**
- Unique customers: **222**
- Delivered orders: **359 (71.8%)**
- Returned + cancelled orders: **50 (10.0%)**
- Home & Kitchen revenue: **$24,591.44**
- Electronics revenue: **$24,183.11**

## RFM methodology

Recency, Frequency, and Monetary values are calculated per customer. Each component receives a 1–5 quintile score. The segmentation logic follows the supplied project specification:

- Champions
- Loyal Customers
- Potential Loyalists
- At Risk
- Lost Customers

## Forecasting

Monthly revenue is indexed sequentially. The project evaluates:

1. Linear Regression
2. Gradient Boosting Regressor

Metrics are Mean Absolute Error (MAE) and R². The supplied report records Gradient Boosting at R² **0.991** and MAE **$318.50** using its stated sequential modeling approach; the included script recomputes the metrics directly from the transaction dataset.

## Run locally

```bash
pip install -r requirements.txt
python eda_sales_analysis.py --data ecommerce_sales_data_500.csv --output plots
```

Generated figures are saved under `plots/`.

## Repository structure

```text
.
├── eda_sales_analysis.py
├── requirements.txt
├── README.md
├── ecommerce_sales_data_500.csv
├── ecommerce_sales_analytics_report.pdf
└── plots/
    ├── category_revenue.png
    ├── monthly_sales_trend.png
    ├── rfm_segments.png
    ├── fulfillment_status.png
    └── payment_methods.png
```

## Business insights

Home & Kitchen and Electronics together account for more than 75% of revenue. RFM analysis identifies a meaningful Champion/Loyal base alongside Lost and At Risk customers, supporting differentiated retention and win-back workflows. Fulfillment analysis highlights the combined return/cancellation rate as an operational improvement area.

## Source basis

The project is grounded in the supplied master specification, sales analytics report, source README, source requirements, source Python script, and transaction CSV.
