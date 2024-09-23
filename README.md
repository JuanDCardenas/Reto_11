# Reto_11
### Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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
```
### Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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
```
### Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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
       
```
### Desarrollar un programa que sume los elementos de una columna dada de una matriz.
```python
def suma_columna(matriz_1: list) -> list:
    suma = [0 for _ in range(len(matriz_1))]
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[0])):
            suma[i] += matriz_1[i][j] 
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

```
### Desarrollar un programa que sume los elementos de una fila dada de una matriz.
```python
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

```
