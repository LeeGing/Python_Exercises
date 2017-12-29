#To Do List

arr = []
def todo():
	print ("=======================================================")
	print ("================       TASK LIST      =================")
	print ("=======================================================")
	print ("[1] - Enter Task || [2] View Tasks || [3] - Delete Task")
	print ("=======================================================")
	option = input("Enter your option number: ")
	print ("=======================================================")
	if option == "1" :
		user_input = input("Enter new task: ")
		print ("=======================================================")
		arr.append(user_input)
		print ("Task list has been updated.")
		print ("=======================================================")
		print ("Current Task List: ")
		print (arr)
		todo()
	elif option == "2":
		print ("Current Task List: ")
		print (arr)
		todo()
	elif option == "3":
		print ("Current Task List: ")
		print (arr)
		user_input = int(input("Enter index number of the task to delete: "))
		print ("=======================================================")
		if ((len(arr) - 1) >= user_input):
			del arr[user_input]
			print ("Task list has been updated.")
			print ("=======================================================")
			print ("Current Task List: ")
			print (arr)
			todo()
		else:
			print ("Error - Invalid input.")
			print ("Please try again.")
			todo()
	else: 
		print ("Error - Invalid input.")
		print ("Please try again.")
		todo()
todo()
