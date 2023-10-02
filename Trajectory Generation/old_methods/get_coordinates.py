
import numpy as np
from scipy import ndimage

def get_middle_horizontal_coordinates(binary_matrix, min_size):
    labeled_components, num_components = ndimage.label(binary_matrix)
    component_sizes = np.bincount(labeled_components.ravel())[1:]
    filtered_areas = [i + 1 for i, size in enumerate(component_sizes) if size >= min_size]
    
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

# Create an example binary matrix with 1s and 0s to represent contiguous areas
binary_matrix = np.array([[1, 1, 1, 1, 1, 1, 0, 1, 0],
                           [1, 1, 0, 0, 0, 0, 0, 1, 0],
                           [0, 1, 1, 1, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 0],
                           [1, 0, 1, 0, 1, 1, 1, 0, 0],
                           [0, 0, 1, 0, 0, 0, 1, 1, 0],
                           [1, 0, 1, 0, 0, 0, 0, 0, 0],
                           [1, 0, 1, 0, 0, 0, 0, 1, 0]])

# Define the minimum size desired for the areas
min_size = 3

# Get coordinates of the first element of all contiguous areas
first_element_coordinates = get_middle_horizontal_coordinates(binary_matrix, min_size)

# Display coordinates
print("Coordinates of the first element of contiguous areas:")
for coordinate in first_element_coordinates:
    print(coordinate)