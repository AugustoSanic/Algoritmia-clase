"""
Insertion Sort es un algoritmo de ordenamiento que construye la lista ordenada un elemento a la vez,
tomando cada elemento y colocándolo en su posición correcta con respecto a los elementos ya ordenados.
"""

def insertion_sort(arr):
    # Recorre la lista desde el segundo elemento hasta el final
    for i in range(1, len(arr)):

        # Toma el elemento actual como "key" para comparar con los elementos anteriores
        key = arr[i]
        j = i - 1

        # Compara "key" con los elementos anteriores y los desplaza a la derecha si son mayores
        while (j >= 0) and (key < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
            
        # Coloca "key" en su posición correcta dentro de la parte ya ordenada de la lista
        arr[j + 1] = key

    #retorna array
    return arr
