#Se define la Matriz 3x3
a = [[5, 8, 9], [2, 1, 7], [3, 4, 6]]
#SE define funcion para buscar un valor en la matriz
def valor_a_buscar(a, num):
    for i in range (len(a)):
        for j in range (len(a[i])):
            if a[i][j] == num:
                return (i, j)
#Se elije que numero buscar en la matriz
num1=2
#Se busca el numero en la matriz
valor = valor_a_buscar(a, num1)

#Muestra un mensaje si se encontro o no el valor buscado
if valor:
    print(f" El numero {num1} se encontro en la posicion {valor} de la matriz seleccionada")
else:
    print(f" El numero {num1} no se encontro en la matriz seleccionada")