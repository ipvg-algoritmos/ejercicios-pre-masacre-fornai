lista = [0, 12, 21, 4, 23, 58, 21, 40, 18, 13, 22]
numero_buscado = int(input("Ingresa el número que deseas buscar: "))
if numero_buscado in lista:
    posicion = lista.index(numero_buscado)
    print(f"El número {numero_buscado} se encuentra en la lista en la posición {posicion}.")
else:
    print(f"El número {numero_buscado} no se encuentra en la lista.")