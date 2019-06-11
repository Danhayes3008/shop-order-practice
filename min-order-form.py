import math

"""
Input an amount to have the amount bought removed from the stock level
"""
name = "- golf balls 9pk"
price = 1.99
packSize = 12
sale = input("how many would you like: ")
minStock = 2000
stockLevel = 2250
stockAvailable = stockLevel - int(sale)
stock = int(stockAvailable)
order = minStock - int(stock)
profit = price * int(sale)
get = int(order) / packSize

print('Sale: ', sale, name)
print('cost: ', '£', price)
print('£', profit)
print('Min stock: ', minStock)
print('Stock level: ', stockLevel)
print('Stock available: ', stockAvailable)
print('packs to order: ', round(get))

if int(stock) > minStock:
    print("no stock is needed")
else:
    if int(stock) < minStock:
        print("More stock is needed")
        print("Please order: ", order, name)
