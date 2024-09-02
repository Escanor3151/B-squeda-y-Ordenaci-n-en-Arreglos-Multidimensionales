# Se define la matriz 3x3
a = [[5, 8, 9], [2, 1, 7], [6, 4, 3]]
# Se crea funcion para imprimir la matriz
def imprimir_matriz(a):
    for fila in a:
        print(fila)
# Se crea funcion para ordenar una fila específica utilizando Bubble Sort
def ordenar_fila(a, fila_i):
    fila = a[fila_i]
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    a[fila_i] = fila
# Se imprime matriz original
print("Matriz original:")
imprimir_matriz(a)
# Se indica que fila ordenar
fila_a_ordenar = 2
ordenar_fila(a, fila_a_ordenar)
# Se imprime la matriz con la fila ordenada
print(f"Matriz con la fila {fila_a_ordenar + 1} ordenada:")
imprimir_matriz(a)