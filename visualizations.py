import pandas as pd
import matplotlib.pyplot as plt
from utils import load_data


def plot_closing_line():
    df = load_data()
    for company in df['Company'].unique():
        sub = df[df['Company'] == company].sort_values('Date')
        plt.plot(sub['Date'], sub['Close/Last'], label=company)
    plt.title("Closing Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_volume_bar():
    df = load_data()
    avg_vol = df.groupby('Company')['Volume'].mean()
    avg_vol.plot(kind='bar', color='skyblue')
    plt.title("Average Volume per Company")
    plt.ylabel("Volume")
    plt.grid(axis='y')
    plt.show()


def plot_price_pie():
    df = load_data()
    latest = df.sort_values('Date').groupby('Company').tail(1)
    closing = latest.set_index('Company')['Close/Last']
    closing.plot.pie(autopct='%1.1f%%')
    plt.title("Latest Closing Price Distribution")
    plt.ylabel('')
    plt.show()


def plot_high_low_scatter():
    df = load_data()
    for company in df['Company'].unique():
        sub = df[df['Company'] == company]
        plt.scatter(sub['High'], sub['Low'], alpha=0.5, label=company)
    plt.title("High vs Low Prices")
    plt.xlabel("High")
    plt.ylabel("Low")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_candlestick():
    df = load_data()
    import matplotlib.dates as mdates
    for company in df['Company'].unique():
        sub = df[df['Company'] == company].sort_values('Date')
        plt.figure(figsize=(10,4))
        plt.plot(sub['Date'], sub['Open'], label='Open', color='green')
        plt.plot(sub['Date'], sub['Close/Last'], label='Close', color='red')
        plt.fill_between(sub['Date'], sub['Low'], sub['High'], color='gray', alpha=0.3)
        plt.title(f"Candlestick-style Price Movement - {company}")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.tight_layout()
        plt.show()
