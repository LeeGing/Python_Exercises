#Pig Latin Translator

ay = 'AY'

print ("###################################################################################")
print ("###                             Pig Latin Converter                                ")
print ("###################################################################################")
user_input = input('### Enter a word: ')
print ("###################################################################################")

if len(user_input) > 0 and user_input.isalpha():
  word = user_input.upper()
  first_letter = word[0]
  pig_latin = word[1:len(word)] + first_letter + ay
  print ("### Your word: " + word + ", converted into Pig Latin is: " + pig_latin + ".")
  print ("###################################################################################")
else:
  print ('Error - No word, or more than one word detected. Try again.')
  print ("###################################################################################")
