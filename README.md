# 📊 Business Operations MIS Reporting & Dashboard Automation

## 📌 Project Overview

The **Business Operations MIS Reporting & Dashboard Automation** project is designed to automate business reporting and help management monitor business performance through meaningful data insights.

This project uses the **Brazilian E-Commerce Public Dataset by Olist** to generate daily, weekly, and monthly MIS reports, analyze business performance, monitor operational activities, identify data quality issues, and create interactive Power BI dashboards.

The main objective is to reduce manual reporting work, improve reporting accuracy, and support better business decisions using data.

---

## 🎯 Project Objectives

- Automate daily, weekly, and monthly MIS reports.
- Extract and organize data from multiple sources.
- Analyze revenue, orders, sellers, and product performance.
- Monitor delivery performance and customer reviews.
- Identify operational exceptions and data quality issues.
- Compare actual business performance with management targets.
- Maintain historical KPI records.
- Create interactive dashboards for management review.
- Automate the reporting workflow using Python.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Microsoft Excel | MIS reports, KPI tracking, formulas, and analysis |
| SQL | Data extraction, filtering, aggregation, and analysis |
| Python | Data cleaning, validation, and report automation |
| Pandas | Data manipulation and processing |
| SQLite | Database storage |
| Power BI | Interactive dashboards and visualization |
| Git & GitHub | Version control and project management |

---

## 📂 Dataset Information

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

**Source:** Kaggle

Dataset Link: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset contains historical e-commerce transaction information, including:

- Orders
- Order Items
- Customers
- Products
- Sellers
- Payments
- Customer Reviews
- Product Categories
- Geolocation

The dataset is used to analyze order performance, revenue, delivery operations, seller performance, and customer satisfaction.

---

## 📁 Project Folder Structure

```text
Business_Operations_MIS/
│
├── database/
│
├── excel/
│   └── MIS_Reports.xlsx
│
├── powerbi/
│   └── Business_Operations_MIS.pbix
│
├── python/
│   ├── data_cleaning.py
│   ├── data_validation.py
│   └── generate_reports.py
│
├── reports/
│   ├── daily/
│   ├── historical/
│   ├── monthly/
│   ├── weekly/
│   │
│   ├── category_performance_sql.csv
│   ├── customer_reviews_sql.csv
│   ├── data_audit_sql.csv
│   ├── delayed_delivery_sql.csv
│   ├── MIS_Reports.xlsx
│   ├── operational_performance_sql.csv
│   ├── revenue_comparison_sql.csv
│   └── seller_performance_sql.csv
│
├── sql/
│   ├── mis_queries.sql
│   └── schema.sql
│
├── venv/
│
├── .gitignore
├── README.md
├── requirements.txt
└── run_pipeline.bat
```

---

## ⚙️ Project Implementation

### Phase 1: Data Collection and Preparation

**Step 1: Project Setup**
- Created the project folder structure.
- Set up Python virtual environment.
- Installed the required Python libraries.
- Organized raw and processed datasets.

**Step 2: Dataset Collection**
- Downloaded the Olist e-commerce dataset.
- Identified the relevant CSV files.
- Reviewed the structure and columns of each dataset.

**Step 3: Data Cleaning**
- Handled missing values.
- Converted date columns into appropriate formats.
- Removed or handled duplicate records where applicable.
- Prepared clean datasets for reporting.

**Step 4: Data Validation**
- Checked missing values and duplicate records.
- Validated important business fields.
- Identified data quality issues.
- Generated data validation reports.

### Phase 2: Database and MIS Reporting

**Step 5: Database Creation**
- Created an SQLite database.
- Designed database tables.
- Loaded processed data into the database.

**Step 6: SQL Analysis**
Created SQL queries to generate:
- Daily MIS reports
- Weekly MIS reports
- Monthly MIS reports
- Category performance reports
- Seller performance reports
- Delayed delivery reports
- Customer review reports
- Data quality reports
- Revenue comparison reports
- Operational performance reports

**Step 7: Excel MIS Reports**

Created Excel reports for:
- Daily performance monitoring
- Weekly business performance
- Monthly revenue analysis
- Category performance
- Seller performance
- Customer reviews
- Delivery performance
- Data quality monitoring

Used Excel formulas, tables, filters, and charts to make reports easier to understand.

**Step 8: MIS Report Analysis**
- Analyzed revenue and order trends.
- Compared seller and category performance.
- Reviewed delivery delays.
- Evaluated customer feedback.
- Identified important business exceptions.

### Phase 3: Automation and Management Reporting

**Step 9: Python Report Automation**
- Automated data cleaning and processing.
- Generated MIS reports using Python.
- Created a batch file to run the reporting pipeline.
- Organized generated reports into separate folders.

**Step 10: Customized Management Reports**

Prepared customized reports for management review:

1. Management Summary
2. Seller Performance Report
3. Operational Exceptions Report

These reports provide a clear view of business performance and areas that need attention.

**Step 11: Historical Data and KPI Tracking**
- Maintained historical MIS reports.
- Created a KPI Tracker in Excel.
- Compared actual performance against sample management targets.
- Calculated KPI achievement percentages.
- Maintained historical records for future comparisons.

### Phase 4: Power BI Dashboard Development

**Step 12: Power BI Data Integration**
- Imported MIS reports into Power BI.
- Checked data types.
- Created a DateTable.
- Established relationships between relevant tables.

**Step 13: KPI Measures and Calculations**
Created DAX measures to calculate:
- Total Revenue
- Total Orders
- Average Order Value
- Delivered Orders
- Average Delivery Days
- On-Time Delivery Percentage
- Delayed Orders
- Average Customer Review

**Step 14: Interactive Dashboard Development**

Developed four dashboard sections:

**1. Management Overview**
- Total Revenue
- Total Orders
- Average Order Value
- Delivered Orders
- Monthly Revenue Trend
- Orders by State
- Order Status Distribution

**2. Operational Performance**
- On-Time Delivery Percentage
- Average Delivery Days
- Delayed Orders
- Delivery Status Analysis
- Customer Review Analysis

**3. Product and Seller Performance**
- Category Revenue
- Products Sold
- Seller Revenue
- Top Performing Categories
- Top Performing Sellers
- Seller State Analysis

**4. Data Quality Monitoring**
- Total Data Issues
- Data Quality Checks
- Missing Data Analysis
- Delayed Order Details
- Customer Review Distribution

### Phase 5: Quality Improvement and Final Review

**Step 15: Data Quality and Financial Discrepancy Checks**
- Reviewed data quality issues before making changes.
- Compared product price and freight charges with total payment.
- Identified financial differences for investigation.
- Avoided automatically changing original financial values.

**Step 16: Report Reconciliation**
- Compared Python-generated and SQL-generated reports.
- Checked important totals and calculations.
- Reviewed differences between report outputs.
- Verified the consistency of key business metrics.

**Step 17: Automation and Performance Improvements**
- Improved the reporting workflow.
- Organized scripts and output files.
- Reviewed data validation rules.
- Identified opportunities for incremental processing.
- Considered ways to reduce manual reporting activities.

**Step 18: Final Documentation and Project Review**
- Organized project files.
- Reviewed Excel reports and SQL queries.
- Verified Python automation.
- Reviewed Power BI dashboards.
- Prepared project documentation for GitHub.

---

## 📈 Key Business KPIs

| KPI | Description |
|---|---|
| Total Revenue | Total payment amount received |
| Total Orders | Number of unique orders |
| Average Order Value | Revenue divided by total orders |
| Delivered Orders | Number of successfully delivered orders |
| Average Delivery Days | Average time taken to deliver orders |
| Delayed Orders | Number of orders delivered after the estimated date |
| On-Time Delivery % | Percentage of eligible delivered orders delivered on time |
| Average Review Score | Average customer review rating |
| Category Revenue | Revenue generated by each product category |
| Seller Revenue | Revenue generated by each seller |

---

## 🔄 Project Workflow

```text
Raw Dataset
     |
     ▼
Data Cleaning (Python)
     |
     ▼
Data Validation
     |
     ▼
SQLite Database
     |
     ▼
SQL Queries and Analysis
     |
     ▼
MIS Report Generation
     |
     ├── Excel Reports
     |
     ├── Daily Reports
     ├── Weekly Reports
     ├── Monthly Reports
     |
     ▼
Python Automation
     |
     ▼
Power BI Dashboards
     |
     ▼
Management Insights
     |
     ▼
Business Decision Making
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YUKTI0807/Business_Operations_MIS
```

### 2. Open the Project Folder

```bash
cd Business_Operations_MIS
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 6. Add the Dataset

Download the Olist dataset from Kaggle and place the original CSV files inside:

```text
data/raw/
```

### 7. Run the Data Cleaning Script

```bash
python python/data_cleaning.py
```

### 8. Run the Data Validation Script

```bash
python python/data_validation.py
```

### 9. Generate MIS Reports

```bash
python python/generate_reports.py
```

### 10. Run the Complete Pipeline

On Windows, execute:

```bash
run_pipeline.bat
```

**Note:** The SQL scripts can be executed against the SQLite database. Open `powerbi/MIS_Dashboard.pbix` in Power BI Desktop to view the dashboards after the required data files and database have been generated.

---

## 💡 Business Value of the Project

This project demonstrates how data can be converted into useful business information.

- **Time Saving:** Reduces repetitive manual reporting activities.
- **Better Accuracy:** Uses validation and reconciliation checks.
- **Performance Monitoring:** Helps management track important KPIs.
- **Operational Improvement:** Highlights delivery delays and other exceptions.
- **Business Insights:** Identifies revenue, category, and seller trends.
- **Decision Support:** Provides interactive dashboards for management review.

---

## 🎓 Skills Demonstrated

- MIS Reporting
- Business Operations Analysis
- Data Cleaning and Validation
- Excel Reporting and Dashboarding
- SQL Queries and Database Management
- Python Automation
- Data Analysis using Pandas
- Power BI Dashboard Development
- KPI Monitoring
- Data Reconciliation
- Business Performance Analysis
- Report Documentation

---

## 🔮 Future Enhancements

- Automate scheduled report generation.
- Connect dashboards to a live business database.
- Implement incremental data processing.
- Add automated email delivery of MIS reports.
- Create advanced forecasting and trend analysis.
- Add alerts for important operational exceptions.

---

## 👩‍💻 Author

**Yukti Sutariya**

Business Operations MIS Reporting & Dashboard Automation

**Tools:** Excel | SQL | Python | Power BI

---

## ⭐ Conclusion

The Business Operations MIS Reporting & Dashboard Automation project brings together Excel, SQL, Python, and Power BI to create an organized reporting workflow.

It helps transform raw e-commerce data into structured MIS reports, track business KPIs, identify operational issues, and present meaningful insights through interactive dashboards.

This project demonstrates practical skills in MIS reporting, business analysis, data automation, and management reporting.
