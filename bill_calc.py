# Restaurant Bill Calculator
print ("==============================")
print ("= Restaurant Bill Calculator =")
print ("==============================")
print ("= Tax - 5%                   =")
print ("= Tip - 12%                  =")
print ("==============================")
meal_cost = float(input("Enter an Amount: $"),)
print ("==============================")
tax = 0.05
tip = 0.12
meal_tax = meal_cost * tax
meal_w_tax = meal_tax + meal_cost
meal_tip = meal_w_tax * tip 
total = meal_w_tax + meal_tip

print ("Total: $" + "%.2f" % total)
