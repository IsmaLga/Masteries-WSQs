#Ismael Lizarraga Gonzalez A01630333
def total(l):
	x=0
	y=0
	while (x<10):
		y=y+(l[x])
		x=x+1
	return y
def average(l):
	x=t/10
	return x
def stdevi(l):
	x=0
	y=0
	z=0
	while (x<10):
		y=((l[x])-a)**2
		x=x+1
		z=z+y
	import math
	w=math.sqrt(z/a)
	return w
l=[]
nums=0
print("Lists")
while(nums<10):
	n=float(input("Give me a number: "))
	l.append(n)
	nums=nums+1
t=total(l)
a=average(l)
sd=stdevi(l)
print("Total: ", t)
print("Average: ", a)
print("Standar Deviation: ", sd)
