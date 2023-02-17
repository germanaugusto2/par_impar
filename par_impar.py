x =int(input("Digite el valor de x: "))

r = x%2

if r==0:
    msj= "par"

else:
    msj= "impar"

print("El numero " + str(x) + " es "+ msj)