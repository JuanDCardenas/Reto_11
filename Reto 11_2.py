def multiplicacion_matrices (matriz_1:list,matriz_2:list)->list:
    if len (matriz_1[0])==len(matriz_2):
        matriz_resultado= [[0 for _ in range(len(matriz_1))] for _ in range(len(matriz_2[0]))]
        for i in range(len(matriz_1)):
            for j in range(len(matriz_2[0])):
                for k in range(len(matriz_1[0])):
                    matriz_resultado[i][j]+=matriz_1[i][k]*matriz_2[k][j]
        return matriz_resultado
    else:
        return "Matrices no validas"
if __name__ == "__main__":
    matriz_1= [
    [7, 8],
    [9, 10],
    [11, 12]
    ]   

    matriz_2= [
    [1, 2, 3],
    [4, 5, 6]
    ]
    resultado=multiplicacion_matrices(matriz_1,matriz_2)
    for i in range(len(resultado)):
        print(resultado[i])