#To Do List

arr = []
def todo():
	print ("=========================================================")
	print ("=================       TASK LIST      ==================")
	print ("=======================================================")
	print ("[1] - ENTER TASK || [2] VIEW TASKS || [3] - DELETE A TASK")
	print ("=========================================================")
	option = input("Enter your option number: ")
	print ("=========================================================")
	if option == "1" :
		user_input = input("ENTER NEW TASK: ")
		print ("=========================================================")
		arr_input = user_input.upper()
		arr.append(arr_input)
		print ("TASK LIST HAS BEEN UPDATED.")
		print ("=========================================================")
		print ("CURRENT TASK LIST: ")
		print (arr)
		todo()
	elif option == "2":
		print ("CURRENT TASK LIST: ")
		print (arr)
		todo()
	elif option == "3":
		print ("CURRENT TASK LIST: ")
		print (arr)
		user_input = int(input("ENTER THE INDEX NUMBER OF THE TASK TO DELETE: "))
		print ("=========================================================")
		if ((len(arr) - 1) >= user_input):
			del arr[user_input]
			print ("CURRENT TASK LIST: ")
			print ("=========================================================")
			print ("CURRENT TASK LIST: ")
			print (arr)
			todo()
		else:
			print ("ERROR - INVALID TASK.")
			print ("PLEASE TRY AGAIN.")
			todo()
	else: 
		print ("ERROR - INVALID TASK.")
		print ("PLEASE TRY AGAIN.")
		todo()
todo()
