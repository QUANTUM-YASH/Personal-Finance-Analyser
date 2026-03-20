import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def pie_chart(category_totals):
    # Create a pie chart to visualize the distribution of expenses by category.
    amounts = category_totals['Amount']
    labels = category_totals['Category']
    plt.pie(amounts, labels=labels, autopct='%1.1f%%')
    plt.title("Category-wise Spending")

def plot_daily_trend(daily_trends):
    # Create a line plot to visualize daily spending trends over time.
    plt.figure(figsize=(8,5))
    plt.plot(daily_trends['Date'], daily_trends['Amount'], marker='o', color='orange')
    plt.title("Daily Spending Trend")
    plt.xlabel("Date")
    plt.ylabel("Amount Spent")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.xticks(rotation=45)   # Makes dates readable
    plt.grid(True)
    plt.tight_layout()
    
def show_plots():
    plt.show()

