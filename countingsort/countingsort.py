"""
Counting Sort es un algoritmo de ordenamiento que se utiliza para ordenar números enteros no negativos.
Funciona contando la frecuencia de cada número en la lista de entrada, luego usa esa información
para colocar los números en la posición correcta en una lista ordenada.
"""

def counting_sort(arr):

    # Verifica si la lista está vacía, si lo está, retorna una lista vacía
    if not arr: 
        return []

    # Obtiene la longitud de la lista y el valor máximo en la lista (k)
    n = len(arr)
    k = max(arr) + 1  # 'k' es el valor máximo más uno para ajustar el índice

    # Crea un arreglo auxiliar 'C' de tamaño 'k', inicializado en 0
    C = [0] * k

    # Recorre la lista original y cuenta la aparición de cada número en 'C'
    for i in range(n):
        C[arr[i]] += 1

    # Transforma el arreglo 'C' para que cada posición contenga la suma de las anteriores
    for i in range(1, k):
        C[i] = C[i] + C[i - 1] 

    # Crea un nuevo arreglo 'B' para almacenar la lista ordenada
    B = [None] * len(arr)

    # Recorre la lista original en orden inverso para colocar los elementos en el arreglo 'B'
    for i in range(n - 1, -1, -1):
        C[arr[i]] -= 1
        B[C[arr[i]]] = arr[i]
    
    # Devuelve sorted list
    return B
