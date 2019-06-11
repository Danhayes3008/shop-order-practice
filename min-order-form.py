"""
Input an amount to have the amount bought removed from the stock level
"""

sale = input(" ")
maxStock = 2500
minStock = 2000
stockLevel = 2250
stockAvailable = stockLevel - int(sale)
stock = int(stockAvailable)
order = minStock - int(stock)

print('Sale: ', sale)
print('Max stock: ', maxStock)
print('Min stock: ', minStock)
print('Stock level: ', stockLevel)
print('Stock available: ', stockAvailable)

if int(stock) > minStock:
    print("no stock is needed")
else:
    if int(stock) < minStock:
        print("More stock is needed")
        print("Please order: ", order, "boxes")
