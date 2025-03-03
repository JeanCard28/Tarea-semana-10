def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de valores

# Matriz 3x3 con valores numéricos
matriz = [
    [3, 1, 9],
    [6, 2, 8],
    [7, 5, 4]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar la fila a ordenar
fila_ordenar = int(input("Ingresa el número de la fila que deseas ordenar (0, 1 o 2): "))

# Verificar si la fila es válida
if 0 <= fila_ordenar < len(matriz):
    bubble_sort(matriz[fila_ordenar])  # Ordenar la fila seleccionada

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("Número de fila inválido. Debe ser 0, 1 o 2.")