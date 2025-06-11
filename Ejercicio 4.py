suma = 0
contador = 0
while True:
    numero = float(input("Ingrese un número (negativo para terminar): "))
    if numero < 0:
        break
    suma += numero
    contador += 1
if contador > 0:
    promedio = suma / contador
    promedio = round(promedio, 2)
    print("El promedio es:", promedio)
else:
    print("No se ingresaron números válidos.")