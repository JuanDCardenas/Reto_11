def suma_de_matrices(matriz_1: list, matriz_2: list) -> list:
    if len(matriz_1) != len(matriz_2) or len(matriz_1[0]) != len(matriz_2[0]):
        return "Matrices no válidas"
    else:
        matriz_resultante = [[0] * len(matriz_1[0]) for h in range(len(matriz_1))]
        for i in range(len(matriz_1)):
            for j in range(len(matriz_1[0])):
                matriz_resultante[i][j] = matriz_1[i][j] + matriz_2[i][j]
        return matriz_resultante

def resta_de_matrices(matriz_1: list, matriz_2: list) -> list:
    if len(matriz_1) != len(matriz_2) or len(matriz_1[0]) != len(matriz_2[0]):
        return "Matrices no válidas"
    else:
        matriz_resultante = [[0] * len(matriz_1[0]) for h in range(len(matriz_1))]
        for i in range(len(matriz_1)):
            for j in range(len(matriz_1[0])):
                matriz_resultante[i][j] = matriz_1[i][j] - matriz_2[i][j]
        return matriz_resultante

if __name__ == "__main__":
    matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    resultado_suma = suma_de_matrices(matriz_1, matriz_2)
    for i in resultado_suma:
        print(i)
    resultado_resta = resta_de_matrices(matriz_1, matriz_2)
    for i in resultado_resta:
        print(i)
