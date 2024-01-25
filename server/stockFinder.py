import requests
import os
import pandas as pd
import sqlalchemy as db

engine = db.create_engine('sqlite:///mydatabase.db')

df_ticker_symbols = pd.read_csv('./stocks-list.csv')

# SQLite connection (replace 'sqlite:///mydatabase.db' with your desired database connection string)
engine = db.create_engine('sqlite:///mydatabase.db')

# Store the DataFrame in a SQL table (replace 'news_sentiment' with your preferred table name)
df_ticker_symbols.to_sql('Ticker_Symbols', con=engine, if_exists='replace', index=False)

class StockFinder:

    def by_symbol(self, symbol):
        uppercaseSymbol = str(symbol).upper()
        query = f'SELECT * FROM Ticker_Symbols WHERE Symbol="{uppercaseSymbol}"'
        return pd.read_sql_query(query, engine)

    def by_name(self, name):
        query = f'SELECT * FROM Ticker_Symbols WHERE "Company Name" LIKE"{name}%"'
        print(name)
        return pd.read_sql_query(query, engine)

    def by_market_cap_range(self, min_cap, max_cap):
        # Implement sentiment analysis algorithm here
        pass
    
    def by_industry(self, industry):
        query = f'SELECT * FROM Ticker_Symbols WHERE Industry="{industry}"'
        return pd.read_sql_query(query, engine)
