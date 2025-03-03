def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición del valor encontrado
    return None  # Retorna None si no se encuentra el valor

# Matriz 3x3 con valores numéricos
matriz = [
    [7, 9, 32],
    [2, 3, 13],
    [4, 8, 17]
]

# Valor a buscar
valor_buscado = int(input("Ingresa el número a buscar: "))

# Buscar el valor en la matriz
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar resultado
if posicion:
    print(f"El número {valor_buscado} se encontró en la posición {posicion}.")
else:
    print(f"El número {valor_buscado} no se encuentra en la matriz.")