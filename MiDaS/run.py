from initialize_variables import *
from MiDaS_depth_estimation import estimate_depth
from choose_angle import choose_angle
from show_depth_image import show_depth_image
from load_model import load_model
from drone import Drone
from scipy import ndimage
import torch

import time
import numpy as np
import torch.nn.functional as F
import cv2


def run():

    #load de MiDaS model to be used
    transform,device,midas=load_model(model_type)

    # Create a list to store drones
    drones = []

    for i in range(num_drones):
        drone = Drone(i, 30, 180)
        drones.append(drone)


    #start_time = time.time()  # Register initial time

    #get depth_estimation_matrix
    depth_estimation_matrix=estimate_depth(filename,transform,device,midas)

    
    """end_time = time.time()  # Registra el tiempo de finalización
    elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
    print(f"Tiempo transcurrido: {elapsed_time} segundos")"""


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
        drone.turn(direction)

    """
    show_depth_image(depth_area)
    show_depth_image(bounded_matrix)
    show_depth_image(depth_estimation_matrix)"""


if __name__ == "__main__":
    run()