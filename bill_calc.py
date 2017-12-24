# Restaurant Bill Calculator

meal_cost = 18.92

tax = 0.05
tip = 0.12
meal_tax = meal_cost * tax
meal_w_tax = meal_tax + meal_cost
meal_tip = meal_w_tax * tip 
total = meal_w_tax + meal_tip

print ("%.2f" % total)
