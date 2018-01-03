#Magic 8 Ball

import random
user_input = input("ASK THE 8 BALL YOUR QUESTION: ")
ans = random.randint(1,3)
if ans == 1:
	print ("8 BALL: YES")
elif ans == 2:
	print ("8 BALL: NO")
else:
	print ("8 BALL: ASK ME AGAIN LATER")