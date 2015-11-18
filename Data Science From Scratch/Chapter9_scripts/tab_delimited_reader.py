import csv

def process(date, symbol, closing_price):  # added to make work
    print(str(date)+":"+str(symbol)+":"+str(closing_price))

with open('tab_delimited_stock_prices.txt', 'rt') as f:  # needed to use rt instead of rb
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)
