#Calculadora

x = int(input("valor de x:"))

y = int(input("Valor de y:"))

print ("Que operación desea hacer?")
print ("sumar")
print ("restar")
print ("multiplicar")
print ("dividir")

opcion = input ("Elija una opcion---> ")
if opcion == "sumar":
    print (x+y)
elif opcion == "restar":
    print (x-y)
elif opcion == "multiplicar":
    print  (x*y)
elif opcion == "dividir":
    print (x / y)
else:
    print ( "No hay operacion")