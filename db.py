import mysql.connector
import pandas as pd
from logger_config import logger


def create_mysql_table():
    df = pd.read_csv("data/stock_data.csv")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="patrika@2003",
        database="revaturestock"
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stocks (
            Company VARCHAR(10),
            Date DATE,
            Close_Last FLOAT,
            Volume BIGINT,
            Open FLOAT,
            High FLOAT,
            Low FLOAT
        )
    """)

    cursor.execute("DELETE FROM stocks")  # Clear existing data

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO stocks (Company, Date, Close_Last, Volume, Open, High, Low)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

def query(sql):
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="revstock"
    )
    result = pd.read_sql(sql, conn)
    conn.close()
    return result

# Example usage:
# create_mysql_table()
# print(query("SELECT * FROM stocks LIMIT 5"))
