# programa que calcula la factura de un item
# you can change itbis (iva) as you like

itbis = float(1.18)
currency = input("currency: ")
item = input("item: ")

print("quantity: ", end="")
quantity = int(input())
print(quantity, item)

print('price: ', end="")
price = float(input())
print("it cost", price, currency, "each")


subtotal = (quantity * price)
print(subtotal, currency, "is the subtotal")

print("itbis:", itbis)

calc = (subtotal * itbis)

total = calc
print("your total is", total, currency)
print("thanks for shopping with us, enjoy your items ;)")