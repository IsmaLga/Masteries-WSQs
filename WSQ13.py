def squareroot(n):
	x=n/2
	y=x+1
	while(x!=y):
		z=n/x
		y=x
		x=(x+z)/2
	return x
ans="yes"
while (ans=="yes"):
	n=float(input("Give me a number: "))
	if (n==0):
		print("The square root is: 0")
	elif (n<0):
		print("Error")
	else:
		sqrt=squareroot(n)
		print("The square root is: ", sqrt)
	ans=str(input("Do you want to try another number?"))
