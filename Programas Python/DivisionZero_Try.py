a = float(raw_input("a: "))
b = float(raw_input("b: "))

respuesta = 0

try:
    respuesta = a/b
except:
    print "No se puede dividir por cero."
    
print "La Respuesta %f" %respuesta