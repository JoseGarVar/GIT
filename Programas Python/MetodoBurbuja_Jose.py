#Programa para acomodar listas con el metodo burbuja

lista = [5,6,8,3,4,1,2,7,10,9]
aux = 0

print "Lista sin Acomodar\n" , lista

for i in range(10):
    for j in range(10):
        if lista[j] > lista[i]:
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux
            
print "Lista Acomodada\n", lista
            