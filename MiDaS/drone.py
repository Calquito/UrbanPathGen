class Drone:
    def __init__(self, id, speed, field_of_vision,video_source,video_type='video'):
        self.speed = speed
        self.field_of_vision = field_of_vision
        self.id=id
        self.video_source=video_source
        self.video_type=video_type

    def turn(self, direction ):
        turning_instruction="Dron "+str(self.id)+" turning towards "+str(direction)
        print(turning_instruction)
        return turning_instruction
    
