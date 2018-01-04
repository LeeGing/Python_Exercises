#Magic 8 Ball

def shake():
	import random
	user_input = input("ASK THE 8 BALL YOUR QUESTION: ")
	ans = random.randint(1,5)
	if ans == 1:
		print ("8 BALL: PERHAPS, YES")
		shake()
	elif ans == 2:
		print ("8 BALL: UNFORTUNATELY, NO")
		shake()
	elif ans == 3:
		print ("8 BALL: I CAN'T SAY.")
		shake()
	else:
		print ("8 BALL: ASK ME AGAIN LATER")
		shake()
shake()