numero = int(raw_input("Numero: "))

es_primo = True

for divisor in range(2,numero):
    if numero % divisor == 0:
        es_primo = False
        break
    #Break se sale del Bucle y Continue es para saltar el codigo pero regresa al Bucle
        
if es_primo == True:
    print "El Numero es Primo"
else:
    print "El Numero no es Primo"