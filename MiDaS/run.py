from initialize_variables import *
from MiDaS_depth_estimation import estimate_depth
from choose_angle import choose_angle
from show_depth_image import show_depth_image
from identify_routes import identify_routes
from load_model import load_model
from identify_routes import identify_routes

from scipy import ndimage
import torch

import time
import numpy as np
import torch.nn.functional as F
import cv2


def run():

    #load de MiDaS model to be used
    transform,device,midas=load_model(model_type)


    #start_time = time.time()  # Register initial time

    #get depth_estimation_matrix
    depth_estimation_matrix=estimate_depth(filename,model_type,transform,device,midas)

    
    """end_time = time.time()  # Registra el tiempo de finalización
    elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
    print(f"Tiempo transcurrido: {elapsed_time} segundos")"""


    # Convert numpy matrix to PyTorch tensor
    depth_tensor = torch.tensor(depth_estimation_matrix, dtype=torch.float32)

    # Threshold
    threshold = np.max(depth_estimation_matrix)*threshold_fraction

    # Apply threshold
    depth_area = np.array((depth_tensor < threshold).float())

    filtered_matrix=identify_routes(depth_area,depth_area.size//submatrices)

    angles, bounded_matrix= choose_angle(filtered_matrix,image_percentage,submatrices,vision_field_degrees)

    print("There are "+str(len(angles))+" posible routes, in the directions "+ str(angles))

    show_depth_image(bounded_matrix)
    show_depth_image(depth_estimation_matrix)


run()