# print header
print("Price Comparison")
print()

#receive input
price_64 = float(input("Price of 64 oz size:  "))
price_32 = float(input("Price of 32 oz size:  "))
print()

#calculate prices per ounce
price_per_ounce_64 = round((price_64 / 64),2)
price_per_ounce_32 = round((price_32 / 32),2)

#print results
print("Price per oz (64 oz):  " + str(price_per_ounce_64))
print("Price per oz (32 oz):  " + str(price_per_ounce_32))