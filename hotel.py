#Hotel Price Calculator

price = float(input("ENTER HOTEL PRICE PER NIGHT: "))
nights = float(input("ENTER AMOUNT OF NIGHTS: "))
tax = 0.12
total = ((price * nights) * tax) + (price * nights)
print (total)
