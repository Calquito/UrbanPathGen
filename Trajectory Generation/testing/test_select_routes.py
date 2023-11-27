import sys
sys.path.append('Trajectory Generation')

import numpy as np
import pytest
from choose_angle import choose_angle
from UAV import UAV

#HARDWARE DEPENDENT################################################################################

#vision field of the dron camera
field_of_view_x=87 #AI-deck color camera module
field_of_view_y=87 #AI-deck color camera module

#turning accuracy degrees
accuracy=5

#resolution of the camera
resolution_x=9
resolution_y=9

#VIDEO VARIABLES###################################################################################

#the frequency at which a frame is captured for analysis
interval_seconds = 1

#shows video taken by the drones (power intensive, may crash the program)
show_video=False


#take screenshots of every frame that the dron captures
take_screenshots=True

#threshold of depth to be considered a route
threshold_fraction=0.25

#ANALYSIS##########################################################################################

#Prints the time that every iteration takes
print_analysis_time=True


#MIDAS MODELS######################################################################################

#model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)#
#model_type = "MiDaS"


#DRONES CONFIGURATION##############################################################################

#min and max vertical height in mts
min_vertical_height=1.0
max_vertical_height=4.0

drone=UAV(0,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.0,resolution_x,resolution_y,'Trajectory Generation/test_videos/building.mp4','video')

submatrices=drone.field_of_view_x//accuracy

@pytest.mark.parametrize("binary_matrix, expected_routes", [
    (np.array([[1, 1, 1, 1, 1, 1, 0, 1, 0],
               [1, 1, 0, 0, 0, 0, 0, 1, 0],
               [0, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 1, 1, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 1, 0]]), ([-19.333333333333332, -19.333333333333332, 9.666666666666666], [('in front of', 0), ('in front of', 0), ('in front of', 0)])),
    (np.array([[1, 1, 1, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 1, 1, 0],
               [1, 0, 1, 1, 1, 1, 1, 1, 0],
               [1, 0, 1, 0, 0, 0, 0, 1, 0]]),([-19.333333333333332, -19.333333333333332, 0.0], [('in front of', 0), ('in front of', 0), ('in front of', 0)])),
    (np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]),([],[])),
    (np.array([[1, 1, 1, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]), ([-29.0], [('up', 3)])),

])
def test_get_middle_horizontal_coordinates(binary_matrix, expected_routes):
    result = choose_angle(binary_matrix,submatrices,drone)
    
    assert result == expected_routes