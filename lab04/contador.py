contador = 0
suma = 0
while True: 
    numero = input ("Intruduzca un número: ")
    if (numero == "fin"):
        break
    contador = contador + 1
    suma = suma + int(numero)
print("Contador", contador)
print("Suma", suma) 
print("Promedio", suma/contador)
