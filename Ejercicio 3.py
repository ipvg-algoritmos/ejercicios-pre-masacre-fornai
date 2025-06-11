lista_numeros = []
while True:
    numero = float(input("Ingrese sus números (Numero negativo para terminar): "))
    if numero < 0:
        break
    lista_numeros.append(numero)
if lista_numeros:
    mayor = max(lista_numeros)
    menor = min(lista_numeros)
    print(f"Su número mayor es: {mayor}")
    print(f"Su número menor es: {menor}")
else:
    print("No se ingresaron números válidos.")