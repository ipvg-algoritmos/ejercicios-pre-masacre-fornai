positivos = 0
negativos = 0
ceros = 0
suma_diag_principal = 0
suma_diag_secundaria = 0
tablero = [[" ", " ", " "] for _  in range(3)]
matriz = []
def mostrar_tablero():
    print("   0   1   2")
    for i, fila in enumerate(tablero):
        print(f"{i}  " + " | ".join(fila))
        if i < 2:
            print("  ---+---+---")
print("Ingrese sus 9 números para la matriz 3x3:\n")
for i in range(3):
    fila = []
    for f in range(3):
        numero = int(input(f"Ingrese su número en posición [{i}][{f}]: "))
        fila.append(numero)

        tablero[i][f] = str(numero)

        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1

        if i == f:
            suma_diag_principal += numero
        if i + f == 2:
            suma_diag_secundaria += numero
    matriz.append(fila)
print("\nTablero con numeros:")
mostrar_tablero()

print("\nResultados:")
print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)

if suma_diag_principal > suma_diag_secundaria:
    print("La primera diagonal tiene mayor suma.")
elif suma_diag_principal < suma_diag_secundaria:
    print("La segunda diagonal tiene mayor suma.")
else:
    print("Ambas diagonales suman lo mismo.")