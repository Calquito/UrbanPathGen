from MiDaS_depth_estimation import estimate_depth
from choose_angle import choose_angle
from show_depth_image import show_depth_image
from load_model import load_model
from matrix_analysis import *
from drone import Drone
from generate_images import generate_merged_images
import torch
from PIL import Image


def complete_analysis(image,output_name,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees,num_drones,drones):
    #get depth_estimation_matrix
    depth_estimation_matrix=estimate_depth(image,transform,device,midas,)

    # Convert numpy matrix to PyTorch tensor
    depth_tensor = torch.tensor(depth_estimation_matrix, dtype=torch.float32)

    # Threshold
    threshold = np.max(depth_estimation_matrix)*threshold_fraction

    # Apply threshold
    depth_area = np.array((depth_tensor < threshold).float())

    angles, bounded_matrix= choose_angle(depth_area,image_percentage,submatrices,vision_field_degrees)

    print("There are "+str(len(angles))+" posible routes, in the directions "+ str(angles))


    for i in range(num_drones):
        direction = angles[i % len(angles)]
        drone = drones[i]
        turning_instruction = drone.turn(direction)

    generate_merged_images([np.array(Image.open(image)),depth_area,depth_estimation_matrix],output_name)