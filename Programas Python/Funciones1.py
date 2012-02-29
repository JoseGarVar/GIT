def duplicar(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]*2
    return

numeros = [4,8,20,7,3]

duplicar(numeros)

print(numeros)

def ordenar(lista):
    for recorrido in range(1,len(lista)):
        for posicion in range(len(lista)-recorrido):
            if lista[posicion] > lista[posicion + 1]:
                lista[posicion],lista[posicion+1] = lista[posicion+1],lista[posicion]
    return
                
desordenados = [32,5,9,2,54,11,0,9]

ordenar(desordenados)

print desordenados