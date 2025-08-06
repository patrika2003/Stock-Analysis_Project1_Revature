import pandas as pd
from utils import load_data
from logger_config import logger
logger.info("Started generating bar chart for monthly volume.")
logger.info("Top 5 highest closing prices calculated.")


def highest_closing():
    df = load_data()
    top = df.sort_values("Close/Last", ascending=False).head(5)
    print("\nTop 5 Highest Closing Prices:")
    print(top[['Company', 'Date', 'Close/Last']])

    

def avg_volume():
    df = load_data()
    avg_vol = df.groupby('Company')['Volume'].mean().sort_values(ascending=False)
    print("\nAverage Trading Volume per Company:")
    print(avg_vol)

def daily_range_summary():
    df = load_data()
    df['Range'] = df['High'] - df['Low']
    summary = df[['Date', 'Company', 'Range']].groupby(['Company']).mean()
    print("\nAverage Daily Price Range per Company:")
    print(summary)

def most_volatile():
    df = load_data()
    df['Volatility'] = df['High'] - df['Low']
    vol = df.groupby('Company')['Volatility'].std().sort_values(ascending=False)
    print("\nMost Volatile Stocks (Std Dev of Range):")
    print(vol.head())

def trend_text():
    df = load_data()
    print("\nStock Trend Summary:")
    for company in df['Company'].unique():
        sub = df[df['Company'] == company].sort_values('Date')
        if len(sub) >= 2:
            start = sub.iloc[0]['Close/Last']
            end = sub.iloc[-1]['Close/Last']
            change = ((end - start) / start) * 100
            trend = "upward" if change > 0 else "downward"
            print(f"{company}: {trend} trend ({change:.2f}% change)")
