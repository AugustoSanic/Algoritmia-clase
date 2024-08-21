"""
Merge Sort es un algoritmo de ordenamiento que sigue el paradigma "divide y vencerás". 
Divide la lista en dos mitades, las ordena de forma recursiva y luego las combina en una lista ordenada.
"""

import math


def merge(left_arr, right_arr):
    # Inicializa una lista para almacenar los elementos combinados
    merged = []
    i, j = 0, 0

    # Agrega sentinelas (infinito) al final de ambas sublistas para facilitar la fusión
    left_arr.append(math.inf)
    right_arr.append(math.inf)

    # Compara y combina elementos de ambas sublistas en una lista ordenada
    while (left_arr[i] != math.inf) or (right_arr[j] != math.inf):
        if left_arr[i] < right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1

    # Elimina los sentinelas de ambas sublistas
    left_arr.pop()
    right_arr.pop()

    # Devuelve la lista combinada y ordenada
    return merged


def merge_sort(arr):
    # Si la lista tiene un solo elemento o está vacía, ya está ordenada
    if len(arr) <= 1:
        return arr

    # Divide la lista en dos mitades
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Combina las dos mitades ordenadas y devuelve la lista ordenada completa
    return merge(left, right)
