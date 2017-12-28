#Pig Latin Converter
import time

def plc():
	ay = 'AY'
	print ("===================================================================================")
	print ("###                           Pig Latin Converter                               ###")
	print ("===================================================================================")
	user_input = input('=== Enter a word: ')
	print ("===================================================================================")
	if len(user_input) > 0 and user_input.isalpha():
	  word = user_input.upper()
	  first_letter = word[0]
	  pig_latin = word[1:len(word)] + first_letter + ay
	  time.sleep(0.5)
	  print ("Converting...")
	  time.sleep(0.5)
	  print ("Converting...")
	  time.sleep(0.5)
	  print ("Converting...")
	  time.sleep(0.5)
	  print ("===================================================================================")
	  print ("Your word: " + word + ", converted into Pig Latin is: " + pig_latin + ".")
	  print ("===================================================================================")
	  print ("###                                  END                                        ###")
	  print ("===================================================================================")
	  plc()
	else:
	  print ('Error Detected - Try Again...')
	  print ("===================================================================================")
	  time.sleep(1.5)
	  print ('Restarting Pig Latin Converter...')
	  print ("===================================================================================")
	  time.sleep(3)
	  plc()
plc()
