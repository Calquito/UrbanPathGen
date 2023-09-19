class Drone:
    def __init__(self, id, speed, field_of_vision,min_height,max_height,current_height,video_source,video_type='video'):
        self.speed = speed
        self.field_of_vision = field_of_vision
        self.id=id
        self.min_height=min_height
        self.max_height=max_height
        self.current_height=current_height

        self.video_source=video_source
        self.video_type=video_type


    def turn(self, direction ):
        turning_instruction="Dron "+str(self.id)+" turning towards "+str(direction)
        print(turning_instruction)
        return turning_instruction
    
    def set_flight_height(self,flight_height):
        self.current_height=flight_height
        print("Current dron height: "+str(self.current_height))
    
