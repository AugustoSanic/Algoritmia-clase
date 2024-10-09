'''
Comparación de RNGs: Middle Square vs numpy.
'''

import numpy as np
import matplotlib.pyplot as plt

# Middle Square Method
def middle_square(n, seed=1234):
    rand_nums = []
    x = seed

    for _ in range(n):
        x = int(str(x * x).zfill(8)[2:6])   
        if x == 0:  
            x = seed
        rand_nums.append(x)

    return np.array(rand_nums) / 10000

# Función para visualizar los números generados
def visualizar_rngs(ms_numbers, numpy_random_numbers):
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))
    axs[0].imshow(ms_numbers, cmap='gray')
    axs[0].set_title('Middle Square Method - RNG Débil')
    axs[1].imshow(numpy_random_numbers, cmap='gray')
    axs[1].set_title('Numpy - RNG Fuerte')
    plt.show()