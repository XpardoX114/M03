loteria=input("Te a tocado la loteria? ")
if(loteria=="Si")or(loteria=="si")or(loteria=="sI")or(loteria=="SI"):
    print("Puedes ganar 3.000 euros al mes")

casar=input("Te casas con un(a) milloneti? ")
edad=int(input("Que edad tiene? "))
enfermedad=input("Tiene problemas de corazon? ")
soltera=input("Esta soltero(a)? ")
if((casar=="Si")and(edad>=80)and(enfermedad=="Si")and(soltera=="No")):
    print("Puedes ganar 3.000 euros al mes")

estudiar=input("Cuanto has estudiado, mucho o poco? ")
M01=int(input("Que nota has sacado? "))
M02=int(input("Que nota has sacado? "))
M03=int(input("Que nota has sacado? "))
M05=int(input("Que nota has sacado? "))
if((estudiar=="Mucho")and(M01>=9)and(M02==10)and(M03>=8)and((M05>=6)and(M05<=8))):
    print("Puedes ganar 3.000 euros la mes")

Ponderada=((M01*0.30)+(M02*0.40)+(M03*0.25)+(M05*0.05))
if(Ponderada>=8): 
    print("Puedes ganar 3.000 euros al mes")
else:
    print("No puedes ganar 3.000 euros al mes")
    
OTRA MANERA:
Ponderada=((M01*0.30)+(M02*0.40)+(M03*0.25)+(M05*0.05))
if(Ponderada>=8)and(estudiar=="Mucho"):
    print("Puedes ganar 3.000 euros al mes")
else:
    print("No puedes ganar 3.000 euros al mes")
