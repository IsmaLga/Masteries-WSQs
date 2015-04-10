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

print("Este programa calculará el máximo común divisor de dos números")
x = int(input("Ingresa el primer número. Por favor, ingresa un número positivo"))
y = int(input("Ingresa el segundo número. Por favor, ingresa un número positivo"))
print ("El máximo común divisor de los dos números es", gcd(x,y))
