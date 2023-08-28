from MiDaS_depth_estimation import estimate_depth
from choose_angle import choose_angle
from show_depth_image import show_depth_image
from load_model import load_model
from matrix_analysis import *
from drone import Drone
from generate_images import generate_merged_images
import torch



def complete_analysis(drone,image,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees):
    #get depth_estimation_matrix
    depth_estimation_matrix=estimate_depth(image,transform,device,midas)

    # Convert numpy matrix to PyTorch tensor
    depth_tensor = torch.tensor(depth_estimation_matrix, dtype=torch.float32)

    # Threshold
    threshold = np.max(depth_estimation_matrix)*threshold_fraction

    # Apply threshold
    depth_area = np.array((depth_tensor < threshold).float())

    angles, bounded_matrix= choose_angle(depth_area,image_percentage,submatrices,vision_field_degrees)

    #print("There are "+str(len(angles))+" posible routes, in the directions "+ str(angles))



    if(len(angles)>0):
        direction = angles[drone.id % len(angles)]
        turning_instruction = drone.turn(direction)
    else:
        #if there are no routes
        turning_instruction = drone.turn(180)
        

    return depth_area, depth_estimation_matrix,bounded_matrix

    