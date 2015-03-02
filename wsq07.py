a = int(input("Ingresa el primer nmero del rango"))
b = int(input("Ingresa el segundo numero del rango"))
s = 0
r = 0

for s in range(a, b+1):
	r = s +r 

print ("La suma del rango es: ", str(r))

