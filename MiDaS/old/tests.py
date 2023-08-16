class Drone:
    def __init__(self, speed, field_of_vision):
        self.speed = speed
        self.field_of_vision = field_of_vision

    def turn(self, direction):
        print(f"Drone turning towards {direction}.")

def round_robin_assign_directions(directions, drones):
    num_drones = len(drones)
    num_directions = len(directions)
    
    for i in range(num_drones):
        direction = directions[i % num_directions]
        drone = drones[i]
        drone.turn(direction)

# Create a list of drone instances
drones = [Drone(30, 120), Drone(25, 90), Drone(40, 150)]

# List of directions to be assigned to drones using Round Robin
directions = ["north", "east"]

# Assign directions using Round Robin and repeat the first direction if needed
round_robin_assign_directions(directions, drones)