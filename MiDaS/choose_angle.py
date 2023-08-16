from matrix_analysis import *
from show_depth_image import show_depth_image
from scipy import ndimage


def choose_angle(depth_estimation_matrix,image_percentage,submatrices,vision_field_degrees):

    adjusted_matrix=remove_extra_columns(depth_estimation_matrix,submatrices)

    #start_row to sum it in case of needing the y coordinate
    bounded_matrix, start_row = select_center_rows(adjusted_matrix,image_percentage)

    #submatrix NxN dimension
    submatrix_dimension=bounded_matrix.shape[1]//submatrices

    center_x = depth_estimation_matrix.shape[1] // 2

    # Define the minimum size desired for the areas
    min_size = bounded_matrix.size//submatrices

    # Get coordinates of the first element of all contiguous areas
    middle_horizontal_coordinates = get_middle_horizontal_coordinates(bounded_matrix, min_size)
    
    angles = []

    for coordinate in middle_horizontal_coordinates:
        distance = coordinate[1] - center_x 
        angle=(distance/depth_estimation_matrix.shape[1])*vision_field_degrees
        angles.append(angle)

        
    return angles, bounded_matrix

