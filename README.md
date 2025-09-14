# Vendor Performance Analysis Report

## 📌 Project Overview  
This project analyzes **vendor and inventory performance** using real-world datasets with crores of records.  
The aim was to design an **ETL pipeline**, clean large noisy datasets, and generate actionable insights through SQL, Python, and interactive visualizations.

🔗 **Live Dashboard:** [Vendor Analysis](https://soyelhossain-stack.github.io/Vendor-Analysis/)  

---

## 🗂️ Data Sources  
The raw datasets (in CSV format) contained transactional and inventory data, including:  
- `begin_inventory.csv` – Opening stock levels  
- `end_inventory.csv` – Closing stock levels  
- `purchase_prices.csv` – Vendor purchase price list  
- `purchases.csv` – Procurement transactions  
- `sales.csv` – Sales transactions  
- `vendor_invoice.csv` – Vendor billing data  

These datasets included **crores of records** with real-world noise and corrupt rows.

---

## ⚙️ Data Engineering Workflow  
### 1. **Data Ingestion**  
- Created a **SQLite database** (`inventory.db`).  
- Designed tables corresponding to each dataset.  
- Automated ingestion via `ingestion.py` (handles loading, logging, error tracking).  

### 2. **Data Cleaning & ETL**  
- Implemented cleaning pipeline in `ETL_pipeline_script.py`:  
  - Removed corrupt/malformed rows.  
  - Standardized date formats, numeric columns, and categorical values.  
  - Deduplicated and validated records.  
- Loaded **cleaned datasets** back into the database.  

### 3. **Reporting Tables**  
- **Product Report** – KPIs per product (sales, revenue, contribution, margin).  
- **Customer Report** – KPIs per customer (spend, frequency, recency, segments).  

---

## 📊 Analysis Performed  
The cleaned data was used for multiple types of business analysis:  

1. **Changes Over Time** – Sales, purchases, and inventory trends across time periods.  
2. **Cumulative Analysis** – YTD / MTD cumulative metrics.  
3. **Segmentation** – Customer and product segmentation based on KPIs.  
4. **Part-to-Whole Analysis** – Contribution of vendors/products to overall sales.  
5. **Performance Analysis** – Vendor scorecards (lead time, invoice accuracy, margin contribution).  

---

## 📈 Results & Visualizations  
- Interactive dashboards and plots were created with **Plotly**.  
- A static **index.html** file was generated for offline access.  
- Visuals include:  
  - Time-series charts of sales & purchases.  
  - Treemaps and pie charts for contribution analysis.  
  - Vendor performance comparison dashboards.  

👉 Explore the live dashboard here: [Vendor Analysis](https://soyelhossain-stack.github.io/Vendor-Analysis/)  

---

## 🔑 Key Learnings  
- Handling **large noisy datasets** with crores of rows in Python & SQL.  
- Building a complete **ETL pipeline**: ingestion → cleaning → loading → reporting.  
- Designing reporting tables for faster analysis.  
- Using Plotly for interactive data storytelling.  

---

## 🚀 Future Enhancements  
- Automate daily ingestion with a scheduler (Airflow/Prefect).  
- Move from SQLite to **PostgreSQL** for scalability.  
- Enhance vendor scorecards with **predictive analytics**.  
- Integrate dashboards into a BI tool (Power BI / Tableau).  
