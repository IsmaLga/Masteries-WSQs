#Ismael Lizárraga González A01630333 

def factorial(n):
	a = n
	b = 1
	while (a > 1):
		b = b * a
		a = a - 1
	return b
	
x = "y"
while (x=="y"):

	n= int(input("Insert integer: "))
	f= factorial(n)

	if (n < 0):
		print("Enter a positive number ")
	else:
		print("The factorial of" , n, "is", f)
		x = input ("Would you like to try another number?" "y/n?" )
else:
	print ("Ten un lindo día ;)")
	
	
