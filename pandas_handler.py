import pandas as pd
import os

def process_expense_data(file_path):
    """
    Automated pipeline to clean, validate, and structure expense data.
    """
    if not os.path.exists(file_path):
        return "❌ Error: Source file not found.", None, None

    try:
        # 1. Load Raw Data
        df = pd.read_csv(file_path)
        print("✅ System: Data loaded. Starting cleaning process...")

        # 2. Automated Cleaning (The 'Data Engineer' Role)
        
        # Remove completely empty rows
        df.dropna(how='all', inplace=True)

        # Standardize Amount: Remove currency symbols and convert to float
        df['Amount'] = df['Amount'].astype(str).str.replace(r'[^0-9.]', '', regex=True)
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

        # Standardize Date: Convert various formats into YYYY-MM-DD
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        # Standardize Category: Trim spaces and capitalize (e.g., 'food ' -> 'Food')
        df['Category'] = df['Category'].astype(str).str.strip().str.title()

        # Drop rows that remain invalid (missing critical values)
        df.dropna(subset=['Amount', 'Date', 'Category'], inplace=True)

        # 3. Data Structuring (The 'Data Analyst' Handover)
        
        # Aggregating totals by Category
        category_totals = df.groupby('Category')['Amount'].sum().reset_index()
        
        # Aggregating totals by Date to identify spending trends
        daily_trends = df.groupby('Date')['Amount'].sum().reset_index()

        # 4. Save Clean Copy
        df.to_csv('cleaned_expenses.csv', index=False)
        
        print("✨ System: Data is now verified and ready for visualization.")
        return category_totals, daily_trends, df

    except Exception as e:
        return f"❌ Critical Failure: {e}", None, None

# --- Execution Block ---
if __name__ == "__main__":
    process_expense_data('file_path')