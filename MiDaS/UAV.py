#class drone = class UAV

#this class represents the abstraction of the real drone
#it defines the hardware parameters needed for the trajectories generation algorithm
class UAV:
    def __init__(self, id, current_speed, max_speed, field_of_view_x, field_of_view_y,min_height, 
                 max_height, current_height, resolution_x, resolution_y, video_source,video_type='video'):
        self.id=id
        self.current_speed = current_speed
        self.max_speed = max_speed
        self.field_of_view_x = field_of_view_x
        self.field_of_view_y = field_of_view_y
        self.min_height = min_height
        self.max_height = max_height
        self.current_height = current_height
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.video_source = video_source
        self.video_type = video_type

    #changes the direction, turning certain amount of degrees
    def turn(self, direction):
        turning_instruction="Dron "+str(self.id)+" turning towards "+str(direction)
        print(turning_instruction)
        return turning_instruction
    
    #moves to the left or to the right
    def move_horizontally(self, direction):
        turning_instruction="Dron "+str(self.id)+" moving towards "+str(direction)
        print(turning_instruction)
        return turning_instruction

    #changes the flight_height of the drone
    def set_flight_height(self,flight_height):
        self.current_height=flight_height
        print("Current dron height: "+str(self.current_height))

    #changes the current speed of the drone
    def set_current_speed(self,new_speed):
        self.current_speed = new_speed
    
