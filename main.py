import analytics
import visualizations
from logger_config import logger

logger.info("Stock analysis program started.")


def main():
    while True:
        print("""
=== RevStock - Stock Analysis Menu ===
1. Top 5 Highest Closing Prices 
2. Average Volume per Company 
3. Daily Price Range Summary 
4. Most Volatile Stock 
5. Stock Trend Over Time 
6. Closing Price Line Chart
7. Average Volume Bar Chart 
8. Price Range Pie Chart 
9. High vs Low Scatter Plot 
10. Candlestick-style Plot
11. Exit
        """)
        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            analytics.highest_closing()
        elif choice == '2':
            analytics.avg_volume()
        elif choice == '3':
            analytics.daily_range_summary()
        elif choice == '4':
            analytics.most_volatile()
        elif choice == '5':
            analytics.trend_text()
        elif choice == '6':
            visualizations.plot_closing_line()
        elif choice == '7':
            visualizations.plot_volume_bar()
        elif choice == '8':
            visualizations.plot_price_pie()
        elif choice == '9':
            visualizations.plot_high_low_scatter()
        elif choice == '10':
            visualizations.plot_candlestick()
        elif choice == '11':
            print("Exiting RevatureStockanalysis. Bye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
