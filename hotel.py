#Hotel Price Calculator

price = float(input("ENTER HOTEL PRICE PER NIGHT: $"))
nights = float(input("ENTER AMOUNT OF NIGHTS: "))
tax = 0.12
total = str(((price * nights) * tax) + (price * nights))
print ("YOUR TOTAL: $" + "%.2f" % total)
