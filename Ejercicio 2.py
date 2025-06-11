def vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMÑNOPQRSTUVWXYZ"
    total_vocales = 0
    total_consonantes = 0
    for caracter in cadena:
        if caracter in alfabeto:
            if caracter in vocales:
                total_vocales += 1
            else:
                total_consonantes += 1
    return total_vocales, total_consonantes
texto = input("Ingresa una cadena de texto: ")
vocales, consonantes = vocales_consonantes(texto)
print(f"Número de vocales: {vocales}")
print(f"Número de consonantes: {consonantes}")