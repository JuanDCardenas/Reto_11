def matriz_transpuesta (matriz_1:list)->list:
    matriz_resultado=[[0]*len(matriz_1) for h in range(len (matriz_1[0])) ]
    for i in range(len(matriz_resultado)):
       for j in range(len(matriz_resultado[0])):
        matriz_resultado[i][j]+= matriz_1[j][i]
    return matriz_resultado
if __name__== "__main__":
    matriz_1=[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [10, 11, 12]
    ]
    resultado=matriz_transpuesta(matriz_1)
    for i in resultado:
       print (i)
       