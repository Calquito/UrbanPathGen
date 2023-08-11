import numpy as np

def find_min_sum_submatrix(matrix, N):
    rows, cols = matrix.shape
    num_submatrices_rows = rows // N
    num_submatrices_cols = cols // N
    
    min_sum = float('inf')
    min_row, min_col = None, None
    
    for i in range(num_submatrices_rows):
        for j in range(num_submatrices_cols):
            submatrix = matrix[i*N : (i+1)*N, j*N : (j+1)*N]
            submatrix_sum = np.sum(submatrix)
            
            if submatrix_sum < min_sum:
                min_sum = submatrix_sum
                min_row, min_col = i*N, j*N
    
    return min_row, min_col

# Ejemplo de uso
matrix = np.array([
    [10, 20, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

N = 2
min_row, min_col = find_min_sum_submatrix(matrix, N)

print("Coordenadas del primer elemento de la submatriz con la suma mínima:", min_row, min_col)