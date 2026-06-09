
## ejercicio 1 : Media de los elementos de un vector

def media_vector(v):
    return sum(v) / len(v)

# Ejemplo
v = [2, 4, 6, 8]
print("Media:", media_vector(v))



## ejercicio 2 : Suma de los cuadrados de las componentes de un vector

def suma_cuadrados(v):
    return sum(x**2 for x in v)

# Ejemplo
v = [1, 2, 3]
print("Suma de cuadrados:", suma_cuadrados(v))



## ejercicio 3 : Producto escalar de dos vectores

def producto_escalar(v, w):
    if len(v) != len(w):
        return "Error: vectores de distinto tamaño"
    return sum(v[i] * w[i] for i in range(len(v)))

# Ejemplo
v = [1, 2, 3]
w = [4, 5, 6]
print("Producto escalar:", producto_escalar(v, w))



## ejercicio 4 : Producto de un número por un vector

def multiplicar_vector(v, n):
    return [n * x for x in v]

# Ejemplo
v = [1, 2, 3]
n = 5
print("Vector multiplicado:", multiplicar_vector(v, n))



## ejercicio 5 : Sumar un número a cada componente de un vector

def sumar_a_vector(v, n):
    return [x + n for x in v]

# Ejemplo
v = [1, 2, 3]
n = 10
print("Vector resultado:", sumar_a_vector(v, n))



## ejercicio 6 : Mínimo de los elementos de un vector

def minimo_vector(v):
    minimo = v[0]
    for x in v:
        if x < minimo:
            minimo = x
    return minimo

# Ejemplo
v = [5, 2, 9, -1, 4]
print("Mínimo:", minimo_vector(v))



## ejercicio 7 : Máximo de los elementos de un vector

def maximo_vector(v):
    maximo = v[0]
    for x in v:
        if x > maximo:
            maximo = x
    return maximo

# Ejemplo
v = [5, 2, 9, -1, 4]
print("Máximo:", maximo_vector(v))



## ejercicio 8 : Menor y mayor elemento en una matriz m x n

def min_max_matriz(matriz):
    minimo = matriz[0][0]
    maximo = matriz[0][0]

    for fila in matriz:
        for x in fila:
            if x < minimo:
                minimo = x
            if x > maximo:
                maximo = x

    return minimo, maximo

# Ejemplo
matriz = [
    [3, 8, 1],
    [5, -2, 7],
    [4, 6, 0]
]

mn, mx = min_max_matriz(matriz)
print("Mínimo:", mn)
print("Máximo:", mx)



## ejercicio 9 : Suma de cada fila de una matriz m x n

def suma_filas(matriz):
    return [sum(fila) for fila in matriz]

# Ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Suma por filas:", suma_filas(matriz))



## ejercicio 10 : Suma de cada columna de una matriz m x n

def suma_columnas(matriz):
    m = len(matriz)
    n = len(matriz[0])

    resultado = [0] * n

    for i in range(m):
        for j in range(n):
            resultado[j] += matriz[i][j]

    return resultado

# Ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Suma por columnas:", suma_columnas(matriz))



## ejercico 11 : Suma de la diagonal izquierda → derecha (diagonal principal)

def diagonal_principal(matriz):
    n = len(matriz)
    suma = 0

    for i in range(n):
        suma += matriz[i][i]

    return suma

# Ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Diagonal principal:", diagonal_principal(matriz))



## ejercicio 12 : Suma de la diagonal derecha → izquierda (diagonal secundaria)

def diagonal_secundaria(matriz):
    n = len(matriz)
    suma = 0

    for i in range(n):
        suma += matriz[i][n - 1 - i]

    return suma

# Ejemplo
print("Diagonal secundaria:", diagonal_secundaria(matriz))



## ejercicio 13 :  Bordes de la matriz en sentido horario → vector

def bordes_horario(matriz):
    m = len(matriz)
    n = len(matriz[0])
    v = []

    # 1. fila superior
    for j in range(n):
        v.append(matriz[0][j])

    # 2. columna derecha
    for i in range(1, m):
        v.append(matriz[i][n - 1])

    # 3. fila inferior
    if m > 1:
        for j in range(n - 2, -1, -1):
            v.append(matriz[m - 1][j])

    # 4. columna izquierda
    if n > 1:
        for i in range(m - 2, 0, -1):
            v.append(matriz[i][0])

    return v

# Ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Bordes en horario:", bordes_horario(matriz))



## ejercicio 14 : Suma de elementos que forman la letra “N” en la matriz

def suma_letra_n(matriz):
    n = len(matriz)
    suma = 0

    for i in range(n):
        # columna izquierda
        suma += matriz[i][0]

        # diagonal principal
        suma += matriz[i][i]

        # columna derecha
        suma += matriz[i][n - 1]

    return suma

# Ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Suma letra N:", suma_letra_n(matriz))