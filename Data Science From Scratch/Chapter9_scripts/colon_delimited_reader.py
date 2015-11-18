import csv

def process(date, symbol, closing_price):  # added to make work
    print(str(date)+":"+str(symbol)+":"+str(closing_price))
    
with open('colon_delimited_stock_prices.txt', 'rt') as f: # needed to use rt instead of rb

    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        process(date, symbol, closing_price)
        
