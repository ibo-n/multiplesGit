userNumber = input("Tell me a number ") 

userNumber = int(userNumber)

multiplier = 1
while multiplier < 11:
	multiple = userNumber * multiplier 
	print("{} times {} equals {}".format(userNumber, multiplier, multiple))
	multiplier += 1