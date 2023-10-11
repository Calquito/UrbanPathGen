import hardware_interface

#class drone = class UAV
#this class represents the abstraction of the real drone
#it defines the hardware parameters needed for the trajectories generation algorithm
class UAV:
    """
    A class representing Unmanned Aerial Vehicles (UAVs)

    This class allows for modeling the essential characteristics and capabilities required for the system's operation. 
    The system is designed to be used with a fleet of variable numbers of drones, necessitating the creation of an instance for each available real UAV.


    Attributes:
    - ID: Represents the drone's identifier. It should be assigned in ascending order, starting from 0.
    - current_speed: Denotes the UAV's current speed in meters per second. This information is crucial for route selection where the drone needs to adjust its  height.
    - field_of_view_x: Represents the drone's field of view in degrees along the x axis. It is required to determine the range of degrees captured by the camera, aiding in decisions about how much the drone should turn in a particular direction.
    - field_of_view_y: Represents the drone's field of view in degrees along the y axis. It is necessary to determine the  height adjustments the drone must make when needed.
    - min_height: Signifies the minimum operating  height of the drone. This variable is defined based on the intended use.
    - max_height: Corresponds to the maximum operating  height of the drone. It is determined based on the intended use and drone's range limitations.
    - current_height: Indicates the drone's current  height, essential for preventing the drone from exceeding set boundaries. In the case of Crazyflie drones, the FlowDeck sensor can provide this information .
    - resolution_x: The resolution in the x direction of the UAV's camera. It is required to estimate potential route locations in the image.
    - resolution_y: The resolution in the y direction of the UAV's camera. It is required to estimate potential route locations in the image.
    - video_source: Corresponds to the video source for analysis. Using OpenCV, you can specify the camera ID associated with the drone instance.
    - video_type: Represents the type of video being captured with the video_source parameter. Two existing types are 'video' (for video files, such as for testing or pre-existing configurations) and 'camera' (for direct UAV camera video sources).

    Methods:
    - turn(direction): Chooses the direction in which the drone should turn to follow the selected route. The allowed range for drone rotation corresponds to the camera's field of view and is defined from -field_of_view_x/2 to field_of_view_x/2.
    - move_horizontally(direction): Specifies the horizontal direction (left or right) in which the drone should move in case a route is not detected.
    - set_flight_height(flight_height): This method enables the definition of the drone's  height within the established limits.
    - set_current_speed(new_speed): This method allows for defining the speed at which the drone is moving. If it cannot be determined through hardware, you can use the average speed or the drone's maximum speed. 
      In the case of Crazyflie drones, this corresponds to 1 m/s . Adjusting this parameter helps calculate the Worst Case Scenario for distance to a route or obstacle.
    """


    def __init__(self, id, current_speed, field_of_view_x, field_of_view_y,min_height, 
                 max_height, current_height, resolution_x, resolution_y, video_source,video_type='video'):
        self.id=id
        self.current_speed = current_speed
        self.field_of_view_x = field_of_view_x
        self.field_of_view_y = field_of_view_y
        self.min_height = min_height
        self.max_height = max_height
        self.current_height = current_height
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.video_source = video_source
        self.video_type = video_type

    #https://stackoverflow.com/questions/40205996/calling-a-global-function-from-an-inner-class-function-in-python

    #changes the direction, turning certain amount of degrees
    def turn(self, direction):
        turning_instruction="Dron "+str(self.id)+" turning towards "+str(direction)
        print(turning_instruction)
        hardware_interface.turn(self.id,direction)
        return turning_instruction
    
    #moves to the left or to the right
    def move_horizontally(self, direction):
        turning_instruction="Dron "+str(self.id)+" moving towards "+str(direction)
        print(turning_instruction)
        hardware_interface.move_horizontally(self.id,direction)
        return turning_instruction

    #changes the flight_height of the drone
    def set_flight_height(self,flight_height):
        self.current_height=flight_height
        print("Current dron height: "+str(self.current_height))
        hardware_interface.set_flight_height(self.id,flight_height)

    #changes the current speed of the drone
    def set_current_speed(self,new_speed):
        self.current_speed = new_speed
        print("Current dron speed: "+str(self.current_speed))
        hardware_interface.set_current_speed(self.id,new_speed)


