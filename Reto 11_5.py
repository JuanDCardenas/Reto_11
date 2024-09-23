def suma_columna(matriz_1: list) -> list:
    suma = [0 for _ in range(len(matriz_1[0]))]
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[0])):
            suma[j] += matriz_1[i][j] 
    return suma 
if __name__ == "__main__":
    matriz_1 = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [10, 11, 12]
    ]
    suma_total = suma_columna(matriz_1)
    print(suma_total) 
