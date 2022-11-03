cadena = "X-DSPAM-Confidence:0.8475"
inicio = cadena.find(":") + 1
final = len(cadena)
número = float(cadena[inicio:final])
print (número)
print(type(número))