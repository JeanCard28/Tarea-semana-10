# Definimos una matriz tridimensional con temperaturas predefinidas
# Formato: matriz[ciudad][semana][día]
temperaturas = [
    [  # Ciudad 1
        [20, 22, 21, 23, 22, 24, 25],  # Semana 1
        [21, 23, 22, 24, 23, 25, 26],  # Semana 2
        [19, 21, 20, 22, 21, 23, 24],  # Semana 3
        [18, 20, 19, 21, 20, 22, 23]   # Semana 4
    ],
    [  # Ciudad 2
        [18, 19, 20, 21, 20, 22, 23],  # Semana 1
        [19, 20, 21, 22, 21, 23, 24],  # Semana 2
        [17, 18, 19, 20, 19, 21, 22],  # Semana 3
        [16, 17, 18, 19, 18, 20, 21]   # Semana 4
    ],
    [  # Ciudad 3
        [25, 26, 27, 28, 27, 29, 30],  # Semana 1
        [26, 27, 28, 29, 28, 30, 31],  # Semana 2
        [24, 25, 26, 27, 26, 28, 29],  # Semana 3
        [23, 24, 25, 26, 25, 27, 28]   # Semana 4
    ]
]

# Calcular el promedio de temperatura para cada ciudad por semana
for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad {i+1}:")
    for j, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)
        print(f"  Semana {j+1} = {promedio:.2f}°C")
    print()
