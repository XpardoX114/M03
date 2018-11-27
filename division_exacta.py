#Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.
#DIVISOR DE NÚMEROS
#Escriba el dividendo: 14
#Escriba el divisor: 5
#La división no es exacta. Cociente: 2 Resto: 4

#DIVISOR DE NÚMEROS
#Escriba el dividendo: 20
#Escriba el divisor: 4
#La división es exacta. Cociente: 5

#CODIGO:

dividendo=float(input("Indique el dividendo: "))
divisor=float(input("Indique el divisor: "))
if(dividendo<=0 or divisor<=0)or(dividendo<=0 and divisor<=0):
    print("El dividendo i/o el divisor es 0")
else: 
    if(dividendo % divisor):
            print("La division no es exacta. El cociente es", (dividendo//divisor))
            Resultado=(dividendo//divisor), "Resto", (dividendo % divisor)
    else:
        print("La división es exacta. El cociente es", (dividendo//divisor))
