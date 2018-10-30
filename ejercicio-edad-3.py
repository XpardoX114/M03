edad = int(input("Indica tu edad: "))
if ((edad>=18)and(edad<=23)):
    print("Puedes entrar en la sesión de jóvenes.")
if (edad==17):
    print("Puedes entrar en la sesión de jóvenes.")
else:
    print("Con", edad , "no puedes entrar en la sesión de jóvenes.")
    
OTRA MANERA:
edad = int(input("Indica tu edad: "))
if (edad>=18 and edad<=23)or(edad==17):
    print("Puedes entrar en la sesión de jóvenes.")
else:
    print("Con", edad , "no puedes entrar en la sesión de jóvenes.")
