# Restaurant Bill Calculator

print ("==============================")
print ("= Restaurant Bill Calculator =")
print ("==============================")
print ("= Suggested Tax - 5%         =")
print ("= Suggested Tip - 12%        =")
print ("==============================")
meal_cost = float(input("Enter an Amount: $"),)
tax = 0.05
tip = 0.12
meal_tax = meal_cost * tax
meal_w_tax = meal_tax + meal_cost
meal_tip = meal_w_tax * tip 
total = meal_w_tax + meal_tip
print ("==============================")
print ("Total: $" + "%.2f" % total)
print ("==============================")
