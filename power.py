#Exponent Calculator

print ("==============================================")
print ("=============Exponent Calculator==============")	
print ("==============================================")
base = int(input("ENTER BASE NUMBER: "))
print ("==============================================")
exponent = int(input("ENTER EXPONENT NUMBER: "))
print ("==============================================")

def power(base, exponent):  
  result = base ** exponent
  print ("%d to the power of %d is %d." % (base, exponent, result))
  print ("========================================")

power(base,exponent)  
