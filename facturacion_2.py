# programa que calcula una factura 
# you can change itbis (iva) as you like
# pls say sir or ma'am

currency = input("set currency: ")

print("set price: ", end="")
price = float(input())
print(price, currency)

print("itbis percentage is: ", end="")
itbis = float(input())

total = (price * itbis)
print("your total is:", total, currency)
