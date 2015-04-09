def gcd(x,y):
    if x!=y:
        while x==0 or y==0:
            if x==0:
                return y
            else:
                return x
        while x>y:
            return gcd(x-y,y)
        while y>x:
            return gcd(x,y-x)
    elif x==y:
        return x

print("this program will calculate the greates common divisor of two numbers")
r="yes"
while r=="yes":
    while True:
        try:
            a=int(input("please enter the first positive integer number: "))
            break
        except ValueError:
            print("sorry that is not a positive integer number,try again")
    while a<0:
        while True:
            try:
                a=int(input("please enter the first positive integer number: "))
                break
            except ValueError:
                print("sorry that is not a positive integer number,try again")
    while True:
        try:
            b=int(input("please enter the second positive integer number: "))
            break
        except ValueError:
            print("sorry that is not a positive intefer number,try again")
    while b<0:
        while True:
            try:
                b=int(input("please enter the first positive integer number: "))
                break
            except ValueError:
                print("sorry that is not a positive integer number,try again")
    c=gcd(a,b)
    print("the greates common divisor of %s and %s is: %s"%(a,b,c))
    r=input("would you like to try with others numbers? yes or no: ")
    while r!="yes" and r!="no":
        r=input("that is not an option,try again(yes or no)")
