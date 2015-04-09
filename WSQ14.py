def calculate_e(precision):
 n=precision
 e=(1+1/n)**n
 return (e)
precision=int(input("Cuantos decimales necesitas? -> "))
respuesta= calculate_e
print("el numero e, con los decimales",precision," es: ",respuesta)
