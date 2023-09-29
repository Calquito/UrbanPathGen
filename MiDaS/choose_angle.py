from matrix_analysis import get_middle_horizontal_coordinates


def choose_angle(depth_area,submatrices,drone):

    #calculate the center of the 
    center_x = drone.resolution_x // 2
    center_y = drone.resolution_y // 2

    # Define the minimum size desired for the areas
    min_size = depth_area.size//submatrices

    # Get coordinates of the first element of all contiguous areas
    middle_horizontal_coordinates = get_middle_horizontal_coordinates(depth_area, min_size)
    
    #list of angles, and if they are in front of the camera
    angles = []
    areas_in_front_of_camera = []

    for coordinate in middle_horizontal_coordinates:
        #check if the area is directly in front of the camera
        #tuple with (direction,pixels distance from y coordinate of the center of the image to the
        # y coordinate of the center of the area)
        if(int(depth_area[center_y][coordinate[1]])==1):
            areas_in_front_of_camera.append(('in front of',0))
        elif(coordinate[0]<center_y):
            areas_in_front_of_camera.append(('up',center_y-coordinate[0]))
        else:
            areas_in_front_of_camera.append('down',coordinate[0]-center_y)

        #calculate distance from the coordinate to the center of the image
        distance = coordinate[1] - center_x 

        #calculate the angle to take in the x axis (if the route is taken depends on if the route is in front of the dron)
        angle=(distance/depth_area.shape[1])*drone.field_of_view_x

        angles.append(angle)

    return angles, depth_area, areas_in_front_of_camera

