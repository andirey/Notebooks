import csv

today_prices = { 'AAPL' : 90.91, 'MSFT' : 41.68, 'FB' : 64.5 }

with open('comma_delimited_stock_prices.txt', 'wt') as f:  # wb had to be changed to wt
    # in Python3, you get the error:
    #   TypeError: 'str' does not support the buffer interface
    
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])
        
