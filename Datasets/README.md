# 📂 Dataset Information

## ⚠️ Dataset Storage
Due to the **large size of the datasets (over 2.5 GB)**, they could not be uploaded directly to GitHub, since GitHub’s free storage limit for repositories does not support such large files.  

Instead, all datasets used in this project have been securely stored in **Google Drive**.  

🔗 **Access the datasets here:**  
[Google Drive Folder](https://drive.google.com/drive/folders/1KoBDSPaAniqq8mt4fO3rUsLcHK8F2Vtl?dmr=1&ec=wgc-drive-hero-goto)  

---

## 📑 List of Datasets
The following raw CSV files are included in the Google Drive folder:

- `begin_inventory.csv` – Opening stock levels  
- `end_inventory.csv` – Closing stock levels  
- `purchase_prices.csv` – Vendor purchase price list  
- `purchases.csv` – Procurement transactions  
- `sales.csv` – Sales transactions  
- `vendor_invoice.csv` – Vendor billing data  

---

## 📌 Notes
- The datasets are **real-world scale** with **crores of records**, which is why they exceed GitHub’s free storage limits.  
- For reproducibility, you can **download the datasets** from the Drive folder and place them in the local `datasets/` directory of your cloned repository.  
- The ETL scripts (`ingestion.py` and `ETL_pipeline_script.py`) are configured to read the CSV files from the `datasets/` folder.  

---

## 🛠️ How to Use
1. Download the dataset folder from Google Drive.  
2. Create a local folder named `datasets/` inside the project directory.  
3. Place all CSV files inside the `datasets/` folder.  
4. Run the ingestion pipeline:  
   ```bash
   python ingestion.py

