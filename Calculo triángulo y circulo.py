calculo=input("Quieres calcular el área de un triángulo o la del círculo? ")
if(calculo=="triángulo"):
    base=int(input("Indique la base: "))
    altura=int(input("Indique la altura: "))
    solucion_triangulo=(base*altura/2)
    print("El área del triángulo es:",solucion_triangulo)
else:
    if(calculo=="círculo"):
        radio=int(input("Indique el radio: "))
        area=int(input("Indique el área: "))
        solucion_circulo=((radio*radio)*(area))
        print("El área del círculo es:", solucion_circulo)

        
        calculo=input("Quieres calcular el área de un triángulo o la del círculo? ")
if(calculo=="triángulo"):
    base=int(input("Indique la base: "))
    altura=int(input("Indique la altura: "))
    solucion_triangulo=(base*altura/2)
    if(solucion_triangulo>=0):
        print("El número tiene que ser mas grande que 0")
    else:
        print("El área del triángulo es:",solucion_triangulo)
if(calculo=="círculo"):
    radio=int(input("Indique el radio: "))
    area=int(input("Indique el área: "))
    solucion_circulo=(radio*radio*3,14)
    if(solucion_circulo>=0):
        print("El número tiene que ser mas grande que 0")
    else:
        print("El área del círculo es:", solucion_circulo)
