#EJERCICIO:
#Hacer un codigo el cual te indique si el numero es positivo o negativo.
#JUEGO DE PUREBAS:
  #  - Si el número es mas garande que 0
  #  - Si el número es mas pequeño que 0
  #  - Si el número es igual a 0
  #  - Si el numero n es negativo
  #  - Si el 0 es positivo, negativo o neutral

#EL 0 ES POSITIVO:
numero=int(input("Indique un número: "))
if(numero<0):
    print("El número",numero,"es negativo")
if(numero>=0):
    print("El número",numero,"es positivo")

#EL 0 ES NEGATIVO:
numero=int(input("Indique un número: "))
if(numero<=0):
    print("El número",numero,"es negativo")
if(numero>0):
    print("El número",numero,"es positivo")
    
#EL 0 ES NEUTRAL:
numero=int(input("Indique un número: "))
if(numero<0):
    print("El número",numero,"es negativo")
if(numero>0):
    print("El número",numero,"es positivo")
if(numero==0):
    print("El número",numero,"es neutral")
