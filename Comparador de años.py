CAPRADOR DE AÑOS:

anyo_actual=int(input("En que año estamos? "))
anyo_cualquiera=int(input("Indique un año cualquiera: "))

if(anyo_actual==anyo_cualquiera):
    print("Es el mismo año")
else:
    if(anyo_actual<anyo_cualquiera):
        solucion1=(anyo_actual-anyo_cualquiera)
        print("Para llegar a año",anyo_cualquiera,"faltan",solucion1,"años")
    else:
        if(anyo_actual>anyo_cualquiera):
            solucion2=(anyo_cualquiera-anyo_actual)
            print("Para llegar a año",anyo_cualquiera,"faltan",solucion2,"años")
