opcion = "z"

while opcion < "a" or opcion > "c":
    print "a) Adoro Python"
    print "b) Detesto Python"
    print "c) No se lo que es Python"

    opcion = raw_input("Elija una Opcion: ")
    
    if opcion == "a":
        print "Me Alegro."
    elif opcion == "b":
        print "Que Mal."
    elif opcion == "c":
        print "Ya Deberias Conocerlo."   
    else:
        print "Tu Opcion no es Valida"
       