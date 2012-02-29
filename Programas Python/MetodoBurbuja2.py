#Programa para acomodar listas con el metodo burbuposiciona

lista = [5,6,8,3,4,1,2,7,10,9]

print "Lista sin Acomodar\n" , lista

for recorrido in range(1,len(lista)):
    for posicion in range(len(lista) - recorrido):
        if lista[posicion] > lista[posicion + 1]:
            aux = lista[posicion]
            lista[posicion] = lista[posicion + 1]
            lista[posicion + 1] = aux
            
print "Lista Acomodada\n", lista
            