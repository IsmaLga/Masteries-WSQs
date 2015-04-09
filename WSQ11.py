def inverse(x):
    x=str(x)
    x=x[::-1]
    x=int(x)
    return x
print("Calculating whether each value is one of: palidrome, non-lychrel or lychre candidate")

numbers=[]
lychrel=[]

x=int(input("Give the lower bound of numbers to consider: "))
x1=int(input("Give the upper bound of numbers to consider: "))

print ("The range of numbers analyzed goes from %s to %s" %(x,x1))
for i in range(x1-x+1):
    numbers.append(x)
    x=x+1
a=0
b=0
ab=0
for i in numbers:
    y=inverse(i)
    if i==y:
        a=a+1
    else:
        z=i+y
        y1=inverse(z)
        for i1 in range(30):
            if z==y1:
                ab=ab+1
                break
            else:
                z=z+y1
                y1=inverse(z)
                if i1==29:
                    b=b+1
                    lychrel.append(i)
print("the number of natural palindromes is: %s"%(a))
print("the number of non-lychrel numbers is: %s"%(ab))
print("the number of lychrel number candidates is: %s"%(b))
if b!= 0:
    print ("found lychrel numbers: ")
    print (lychrel)
