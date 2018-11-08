#EJERCICIO:
#Hacer un codigo el cual te indique si el numero es positivo o negativo.
#JUEGO DE PUREBAS:
  #  - Si el número es mas garande que 0 (positivo).
  #  - Si el número es mas pequeño que 0 (negativo).
  #  - Si el número es igual a 0.
  #  - Si el 0 es positivo, negativo o neutral.

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

#EJERCICIO 2:
#Leer 2 nombres enteros y mostralos en orden
#JUEGO DE PRUBAS:
   #  - Si los numero son negativos
   #  - Si los numero son positivos
   #  - Si un numero es positivo y otro negativo
   #  - Si un numero es negativo y otro positivo
   #  - Si el numero es 0 y ortro positivo
   #  - Si el numero es 0 y otro negative
   #  - Si los numeros son iguales
    
numero1=int(input("Indica el primer número: "))
numero2=int(input("Indica el segundo número: "))
if(numero1<numero2):
    print(numero1,numero2)
else:
    print(numero2,numero1)
if(numero1==numero2):
    print("Son el mateix número")
    
  #Leer 3 nombres enteros y mostralos en orden
  #JUEGO DE PRUBAS:
   #  - Si los numero son negativos
   #  - Si los numero son positivos
   #  - Si un numero es positivo y los otros 2 negativo
   #  - Si un numero es negativo y los otro 2 positivo
   #  - Si el numero es 0 y ortro positivo
   #  - Si el numero es 0 y otro negative
   #  - Si los numeros son iguales
  
numero1=int(input("Indica el primer número: "))
numero2=int(input("Indica el segundo número: "))
numero3=int(input("Indica el tercer número: "))
if(numero1<numero2<numero3):
    print(numero1,numero2,numero3)
if(numero1<numero3<numero2):
    print(numero1,numero3,numero2)
if(numero2<numero1<numero3):
    print(numero2,numero1,numero3)
if(numero2<numero3<numero1):
    print(numero2,numero3,numero1)
if(numero3<numero1<numero2):
    print(numero3,numero1,numero2)
if(numero2<numero2<numero1):
    print(numero2,numero2,numero1)

if(numero1==numero3<numero2):
    print(numero1,numero3,numero2)
if(numero2==numero1<numero3):
    print(numero2,numero1,numero3)
if(numero2==numero3<numero1):
    print(numero2,numero3,numero1)
if(numero3<numero1==numero2):
    print(numero3,numero1,numero2)
if(numero1==numero2<numero3):
    print(numero1,numero2,numero3)
if(numero2==numero3==numero1): 
    print("Todos los nuemros son los mismos")
