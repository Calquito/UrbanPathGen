from matrix_analysis import *


def choose_angle(depth_area,image_percentage,submatrices,vision_field_degrees):

    #adjusted_matrix=remove_extra_columns(depth_area,submatrices)

    #start_row to sum it in case of needing the y coordinate
    bounded_matrix, start_row = select_center_rows(depth_area,image_percentage)

    #submatrix NxN dimension
    submatrix_dimension=bounded_matrix.shape[1]//submatrices

    center_x = depth_area.shape[1] // 2
    center_y = depth_area.shape[0] // 2

    # Define the minimum size desired for the areas
    min_size = bounded_matrix.size//submatrices

    # Get coordinates of the first element of all contiguous areas
    middle_horizontal_coordinates = get_middle_horizontal_coordinates(bounded_matrix, min_size)
    
    angles = []
    areas_in_front_of_camera = []

    for coordinate in middle_horizontal_coordinates:
        #check if the area is directly in front of the camera
        #tuple with (direction,pixels distance from y coordinate of the center of the image to the
        # y coordinate of the center of the area)
        if(int(bounded_matrix[center_y][coordinate[1]])==1):
            areas_in_front_of_camera.append(('in front of',0))
        elif(coordinate[0]<center_y):
            areas_in_front_of_camera.append(('up',center_y-coordinate[0]))
        else:
            areas_in_front_of_camera.append('down',coordinate[0]-center_y)

        distance = coordinate[1] - center_x 
        angle=(distance/depth_area.shape[1])*vision_field_degrees
        angles.append(angle)

    return angles, bounded_matrix, areas_in_front_of_camera

