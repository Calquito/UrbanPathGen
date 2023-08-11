from initialize_variables import *
from MiDaS_depth_estimation import estimate_depth
from choose_angle import choose_angle
from show_depth_image import show_depth_image


def run():
    depth_estimation_matrix=estimate_depth(filename,model_type)
    angle=choose_angle(depth_estimation_matrix)
    show_depth_image(depth_estimation_matrix)

run()