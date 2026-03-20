import tkinter as tk
from tkinter import filedialog
from pandas_handler import process_expense_data
from graph import pie_chart
from graph import plot_daily_trend
from graph import show_plots

def main():
    # --- File Selection Dialog ---
    root = tk.Tk()
    root.withdraw()
    file_path=filedialog.askopenfilename(title="Select Expense Data CSV File", filetypes=[("CSV files", "*.csv")])
    if not file_path:
        print("❌ No file selected. Exiting.")
        exit()
    else:
        # ---Data Processing---
        cat_summary, daily_trends, full_data=process_expense_data(file_path)

        if full_data is not None:
            print("✅ Data processing complete. Generating visualizations...")
        # --- Visualization ---
            pie_chart(cat_summary)
            plot_daily_trend(daily_trends)
            show_plots()

    # ---Insights---
    print("📊 Insights:")

    if full_data is not None:

        max_cat=cat_summary.loc[cat_summary['Amount'].idxmax()]
        category=max_cat['Category']
        amount=max_cat['Amount']
        print(f" The highest spending category is {category} with a total expenditure of Rs.{amount}")

        max_day=daily_trends.loc[daily_trends['Amount'].idxmax()]
        date=max_day['Date'].strftime('%d-%m-%Y')
        amount1=max_day['Amount']
        print(f" The day with the highest spending is {date} with a total expenditure of Rs.{amount1}")

        avg_spending=daily_trends['Amount'].mean()
        print(f" The average daily spending is Rs.{avg_spending:.2f}")

        sum_cat=cat_summary['Amount'].sum()
        half_sum=sum_cat/2
        prcnt=(max_cat['Amount']/sum_cat)*100
        if max_cat['Amount'] >= half_sum:
            print(f"You are spending {prcnt:.2f}% of your total budget on {category}, which is quite high and may indicate overspending.")
        else:
            print(" No single category dominates the spending, suggesting a more balanced expenditure pattern.")

        line=daily_trends.sort_values('Date')
        if line['Amount'].iloc[-1] > line['Amount'].iloc[0]:
            print(" The overall spending trend is increasing, which may require attention to prevent overspending.")
        elif line['Amount'].iloc[-1] < line['Amount'].iloc[0]:
            print(" The overall spending trend is decreasing, indicating good financial management.")
        else:
            print(" The overall spending trend is stable, suggesting consistent financial habits.")


# ---Execution---
if __name__=='__main__':
    main()