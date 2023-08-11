from matrix_analysis import *
from initialize_variables import *


def choose_angle(depth_estimation_matrix):

    # Decision with angles based on area

    adjusted_matrix=remove_extra_columns(depth_estimation_matrix,submatrices)

    #start_row to sum it in case of needing the y coordinate
    bounded_matrix, start_row = select_center_rows(adjusted_matrix,50)

    #submatrix NxN dimension
    submatrix_dimension=bounded_matrix.shape[1]//submatrices

    #get the coordinates of the first element of the deepest submatrix
    min_row, min_col=find_min_sum_submatrix(bounded_matrix,submatrix_dimension)

    center_x = depth_estimation_matrix.shape[1] // 2


    # Distance between points
    distance = min_col - center_x 

    print("dpx: "+ str(min_col))
    print("dpy: "+ str(min_row))
    print("center: "+str(center_x))

    print("distance: "+str(distance))

    #angle, the center is the zero, negative angle is left, positive angle is right

    angle=(distance/depth_estimation_matrix.shape[1])*180

    print("angle: "+str(angle))

    return angle


