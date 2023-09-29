import numpy as np
from scipy import ndimage
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
    
#keep the indicated percentage of the matrix
def select_center_rows(matrix, percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage has to be between 0 and 100.")
    
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

#takes a binary array and a desired minimum size for the areas, 
#and returns a list of coordinates of the first element of each contiguous area that meets the minimum size. 
def get_first_element_coordinates(binary_matrix, min_size):
    labeled_components, num_components = ndimage.label(binary_matrix)
    component_sizes = np.bincount(labeled_components.ravel())[1:]
    filtered_areas = [i + 1 for i, size in enumerate(component_sizes) if size >= min_size]
    
    first_element_coordinates = []
    for area in filtered_areas:
        indices = np.where(labeled_components == area)
        first_element = (indices[0][0], indices[1][0])  # Get coordinates of the first element
        first_element_coordinates.append(first_element)
    
    return first_element_coordinates

#calculates the row index of the middle horizontal element by averaging 
#the minimum and maximum row indices of the area

def get_middle_horizontal_coordinates(binary_matrix, min_size):
    #ignore areas of small size
    labeled_components, num_components = ndimage.label(binary_matrix)
    component_sizes = np.bincount(labeled_components.ravel())[1:]
    filtered_areas = [i + 1 for i, size in enumerate(component_sizes) if size >= min_size]
    
    #get coordinates
    middle_horizontal_coordinates = []
    for area in filtered_areas:
        indices = np.where(labeled_components == area)
        min_row = min(indices[0])
        max_row = max(indices[0])
        middle_row = (min_row + max_row) // 2
        middle_col = sum(indices[1]) // len(indices[1])  # Calculate the average x-coordinate
        middle_element = (middle_row, middle_col)  # Get coordinates of the middle horizontal element
        middle_horizontal_coordinates.append(middle_element)
    
    return middle_horizontal_coordinates


