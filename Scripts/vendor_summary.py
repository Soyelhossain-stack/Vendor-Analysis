import pandas as pd
import sqlite3
import logging
from ingestion import ingest_db


logging.basicConfig(
    filename= 'logs/vendor_summary.log',
    level= logging.DEBUG,
    format= " %(asctime)s - %(levelname)s - %(message)s ",
    filemode= 'a'
)

def create_vendor_summary(conn):
    Vendor_Sales_Summary = pd.read_sql_query("""
with FreightSummary as (
    SELECT 
        VendorNumber, 
        sum(Freight) as FreightCost
    FROM vendor_invoice
    GROUP BY VendorNumber                                         
),
PurchaseSummary as (
    SELECT 
        p.VendorNumber,
        p.VendorName,
        p.Brand,
        p.Description,
        p.PurchasePrice,
        SUM(p.Dollars) as TotalPurchaseDollars,
        SUM(p.Quantity) as TotalPurchaseQuantity,
        pp.Volume,
        pp.Price as ActualPrice
        FROM purchases as p
        JOIN purchase_prices as pp
        ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY p.VendorNumber, p.VendorName, p.Brand                                   
),
SalesSummary as (
    SELECT 
    VendorNo,
    Brand,
    sum(SalesQuantity) as TotalSalesQuantity,
    sum(SalesDollars) as TotalSalesDollar,
    sum(SalesPrice) as TotalSalesPrice,
    sum(ExciseTax) as TotalExciseTax
    FROM sales
    GROUP BY 
    VendorNo,
    Brand
)
SELECT
    ps.VendorNumber,
    ps.VendorName,
    ps.Brand,
    ps.Description,
    ps.PurchasePrice,
    ps.ActualPrice,
    ps.Volume,
    ps.TotalPurchaseQuantity,
    ps.TotalPurchaseDollars,
    ss.TotalSalesQuantity,
    ss.TotalSalesDollar,
    ss.TotalSalesPrice,
    ss.TotalExciseTax,
    fs.FreightCost       
FROM PurchaseSummary as ps
LEFT JOIN SalesSummary as ss
    ON ps.VendorNumber = ss.VendorNo
    AND ps.Brand = ss.Brand
LEFT JOIN FreightSummary as  fs
    ON ps.VendorNumber = fs.VendorNumber
""", conn)
    
    return Vendor_Sales_Summary

def clean_data(Vendor_Sales_Summary):

    # Changing datatype of VendorName column
    Vendor_Sales_Summary['Volume'] = Vendor_Sales_Summary['Volume'].astype('float64')

    # Filling the null values with Zero
    Vendor_Sales_Summary.fillna(0, inplace= True)

    # Removing unwanted spaces from the VendorName column
    Vendor_Sales_Summary['VendorName'] = Vendor_Sales_Summary['VendorName'].str.strip()

    # Rename Column 
    Vendor_Sales_Summary = Vendor_Sales_Summary.rename(columns={"TotalSalesDollar": "TotalSalesDollars"})

    # Creating New columns for better analysis
    Vendor_Sales_Summary['GrossProfit'] = Vendor_Sales_Summary['TotalSalesDollars'] - Vendor_Sales_Summary['TotalPurchaseDollars'] 
    Vendor_Sales_Summary['ProfitMargin'] = (Vendor_Sales_Summary['GrossProfit'] / Vendor_Sales_Summary['TotalSalesDollars'] ) * 100
    Vendor_Sales_Summary['StockTurnover'] = Vendor_Sales_Summary['TotalSalesQuantity'] / Vendor_Sales_Summary['TotalPurchaseQuantity']
    Vendor_Sales_Summary['SalesPurchaseRatio'] = Vendor_Sales_Summary['TotalSalesDollars'] / Vendor_Sales_Summary['TotalPurchaseDollars']
    
    return Vendor_Sales_Summary

if __name__ == '__main__':
    # Create database connection
    conn= sqlite3.connect('inventory.db')

    logging.info('Creating vendor summary table ......')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning data ......')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())    

    logging.info('Ingesting data ......')
    ingest_db (clean_df, 'vendor_sales_summary', conn)
    logging.info('Completed')
