#This are the methods called by the UAV class
#The implementation of the movement depends on the hardware

def turn(id,direction):
    """
    Choose the direction in which the drone should turn to take the selected route. 
    The range in which the drone can turn corresponds to the field of view of the drone's camera, 
    and is defined from (-field_of_view_x/2) to (field_of_view_x/2)
    where field_of_view corresponds to the field of view of the UAV's camera at x, in degrees.
    0° is the center of the image.

    The drone has to keep moving forward after the turn

    :param direction: The angle at which the drone should turn
    :type direction: float
    """
    # TODO: Implement the functionality here
    pass

#moves to the left or to the right
def move_horizontally(id,direction):
    """
    Choose the direction in which the drone should move if there is no route. 
    Move to the left or to the right

    The drone has to keep moving forward after the moving

    :param direction: The angle at which the drone should move
    :type direction: string
    """

    if(direction=="right"):
        # TODO: Implement the functionality here
        pass
    elif(direction=="left"):
        # TODO: Implement the functionality here
        pass
    else:
        raise ValueError("Wrong direction")


#changes the flight_height of the drone
def set_flight_height(id,flight_height):
    """This method allows to define the height of the drone, within the established limits.
    
    :param flight_height: The new drone flight height, in meters. 
    :type flight_height: float
    
    """
    # TODO: Implement the functionality here
    pass

#changes the current speed of the drone
def set_current_speed(id,current_speed):
    """This method allows to define the current speed of the drone.
    
    :param current_speed: The new drone speed,in meters/second. 
    :type current_speed: float
    
    """
    # TODO: Implement the functionality here
    pass
