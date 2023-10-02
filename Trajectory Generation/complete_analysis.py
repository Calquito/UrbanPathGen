from MiDaS_depth_estimation import estimate_depth
from choose_angle import choose_angle
from matrix_analysis import *
import torch
import time
from math import tan,pi,radians


#if no routes are identified, turn to the left or to the right depending on the dron ID
def handle_no_routes(drone):
    if drone.id % 2 == 0:
        turning_instruction = drone.move_horizontally("right")
    else:
        turning_instruction = drone.move_horizontally("left")


#makes the analysis of the image (depth estimation and route calculation)
def complete_analysis(drone,image,transform,device,midas,threshold_fraction,submatrices,interval_seconds):
    start_time = time.time()
    
    #get depth_estimation_matrix
    depth_estimation_matrix=estimate_depth(image,transform,device,midas)

    # Convert numpy matrix to PyTorch tensor
    depth_tensor = torch.tensor(depth_estimation_matrix, dtype=torch.float32)

    # Threshold
    threshold = np.max(depth_estimation_matrix)*threshold_fraction

    # Apply threshold
    depth_area = np.array((depth_tensor < threshold).float())

    angles, areas_in_front_of_camera = choose_angle(depth_area,submatrices,drone)

    #print("There are "+str(len(angles))+" posible routes, in the directions "+ str(angles))

    #choose route if exists
    if(len(angles)>0):

        #round robin to asign route to a dron
        route_asigned_by_id=drone.id % len(angles)
        direction = angles[route_asigned_by_id]
        if(areas_in_front_of_camera[route_asigned_by_id][0]=="in front of"):
            turning_instruction = drone.turn(direction)
        else:

            #vertical movement estimation
            #worse case scenario distance to obstacle. d=v*t
            wcs_distance_to_route=drone.current_speed*interval_seconds

            #worse case scenario height, using trigonometry
            #tan uses radians, so convert
            alpha = radians(drone.field_of_view_y / 2)

            #this would be the wsc distance in meters equivalent to the pixels of area_height_pixels
            wcs_height=tan(alpha)*wcs_distance_to_route


            #estimate the height to set to the dron based in the worse case scenario
            area_height_meters=wcs_height*(areas_in_front_of_camera[route_asigned_by_id][1]/(drone.resolution_y/2))

            #check that the dron stays within the limits
            if(areas_in_front_of_camera[route_asigned_by_id][0]=="up" and ((drone.current_height+area_height_meters)<=drone.max_height)):
                drone.set_flight_height(drone.current_height+area_height_meters)
            elif(areas_in_front_of_camera[route_asigned_by_id][0]=="down" and ((drone.current_height-area_height_meters)>=drone.min_height)):
                drone.set_flight_height(drone.current_height-area_height_meters)
            else:
                #if there are no routes
                handle_no_routes(drone)
    else:
        #if there are no routes
        handle_no_routes(drone)


    #estimate the time that the analysis take (ideally lower than the interval of capture)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")

    return depth_area, depth_estimation_matrix,depth_area

    