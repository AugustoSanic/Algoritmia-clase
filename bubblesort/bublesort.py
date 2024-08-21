"""
Bubble Sort es un algoritmo de ordenamiento simple que funciona al comparar
pares adyacentes de elementos en una lista y los intercambia si están en el orden incorrecto.
Este proceso se repite múltiples veces hasta que la lista quede completamente ordenada.
"""

def bubble_sort(arr):
    # Obtiene la longitud de la lista que vamos a ordenar
    n = len(arr)

    # Hace un bucle que se ejecutará 'n' veces, donde 'n' es la longitud de la lista
    for _ in range(n):
        # Recorre la lista hasta el penúltimo elemento
        for j in range(n - 1):
            # Compara el elemento actual (arr[j]) con el siguiente (arr[j+1])
            if arr[j] > arr[j+1]:
                # Si el elemento actual es mayor que el siguiente, los intercambia
                # Este intercambio hace que los elementos más grandes se desplacen hacia el final
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # Devuelve la lista ordenada
    return arr
