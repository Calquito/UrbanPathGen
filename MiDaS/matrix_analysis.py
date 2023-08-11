import numpy as np

#acepts np.array
def split_matrix_vertical(matriz):
    # get number of columns of the matriz
    num_columnas = matriz.shape[1]
    
    # split vertically
    parte1 = matriz[:, :num_columnas // 2]
    parte2 = matriz[:, num_columnas // 2:]
    
    # convert each side to array
    array_parte1 = parte1.flatten()
    array_parte2 = parte2.flatten()
    
    return array_parte1, array_parte2

#so the matrix colums is multiple of the accuracy in degrees
def remove_extra_columns(matrix, multiple):
    original_columns = matrix.shape[1]
    required_columns = (original_columns // multiple) * multiple
    
    if required_columns < original_columns:
        return matrix[:, :required_columns]
    else:
        return matrix
    
#keep the indicated percet
def select_center_rows(matrix, percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100.")
    
    num_rows = matrix.shape[0]
    num_center_rows = int(num_rows * (percentage / 100))
    start_row = (num_rows - num_center_rows) // 2
    end_row = start_row + num_center_rows
    
    return matrix[start_row:end_row, :], start_row

#divide the matrix in submatrices, do the sum of values, and return y,x coordinates of the first element
#of the matrix with the lower sum

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