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
ordered = int(get) * packSize
buy = int(order) - int(ordered)

print('Sale: ', sale, name)
print('cost: ', '£', price)
print('£', profit)
print('Min stock: ', minStock)
print('Stock level: ', stockLevel)
print('Stock available: ', stockAvailable)

if int(stock) > minStock:
    print("no stock is needed")
else:
    if int(stock) < minStock:
        print("More stock is needed")
        print("Please order: ", order, name)


if int(ordered) < int(order):
    buy = ordered + packSize
    print('buy: ', ordered + packSize, '- balls')
    print('boxes ordered: ', math.ceil(get), '- Packs')
