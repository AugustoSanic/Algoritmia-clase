def bubble_sort_opt(arr):
    # Obtiene la longitud de la lista que vamos a ordenar
    n = len(arr)

    # Hace un bucle que se ejecutará 'n' veces, donde 'n' es la longitud de la lista
    for i in range(n):
        # Inicializa la variable 'sorted' como True para detectar si se realizaron intercambios
        sorted = True

        # Recorre la lista hasta el penúltimo elemento, acortando la iteración en cada pasada
        for j in range(n - 1 - i):
            # Compara el elemento actual (arr[j]) con el siguiente (arr[j+1])
            if arr[j] > arr[j+1]:
                # Si el elemento actual es mayor que el siguiente, los intercambia
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Indica que se ha realizado un intercambio, por lo tanto, la lista no está ordenada aún
                sorted = False
        
        # Si no se realizaron intercambios en una pasada completa, se considera que la lista está ordenada
        if sorted:
            return arr
        
    # Devuelve la lista ordenada
    return arr