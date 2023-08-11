import numpy as np

def partir_matriz_vertical(matriz):
    # Obtener el número de columnas de la matriz
    num_columnas = matriz.shape[1]
    
    # Dividir la matriz verticalmente en dos
    parte1 = matriz[:, :num_columnas // 2]
    parte2 = matriz[:, num_columnas // 2:]
    
    # Convertir cada parte en un array
    array_parte1 = parte1.flatten()
    array_parte2 = parte2.flatten()
    
    return array_parte1, array_parte2

# Ejemplo de matriz de 3x4
matriz_ejemplo = np.array([[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12]])

# Partir la matriz en dos y convertir cada parte en un array
parte1_array, parte2_array = partir_matriz_vertical(matriz_ejemplo)

print("Parte 1 como array:", np.sum(parte1_array))
print("Parte 2 como array:", np.sum(parte2_array))