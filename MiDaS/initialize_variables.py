from drone import Drone
from load_model import load_model


#HARDWARE DEPENDENT###########################################

#vision field of the dron camera
vision_field_degrees=87 #AI-deck color camera module

#turning accuracy
accuracy=5

#################################################################

#Video variables#################################################

interval_seconds = 5

show_video=False
take_screenshots=True
analyze_screenshots=False

#video resolution can be to big, so to resize it
resize_fraction=0.5

#dron video to show (dron.id has to exist)
dron_to_show=0


between_frame_sleep_time=0.01

###############################################################
#number of submatrices
submatrices=vision_field_degrees//accuracy

#percentaje of the image considererd
image_percentage=100

#threshold fraction
threshold_fraction=0.25

#frecuency_of_images=3

#model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)#
#model_type = "MiDaS"
#model_type = "transforms"

#Variables for complete analysis###############################
#load de MiDaS model to be used
transform,device,midas=load_model(model_type)

# Create a list to store drones
drones = []

drones.append(Drone(0,30,vision_field_degrees,'MiDaS/test_video/building.mp4','video'))
drones.append(Drone(1,30,vision_field_degrees,0,'camera'))
drones.append(Drone(2,30,vision_field_degrees,'MiDaS/test_video/woods.mp4','video'))
drones.append(Drone(3,30,vision_field_degrees,'MiDaS/test_video/woods.mp4','video'))

num_drones=len(drones)

"""
for i in range(num_drones):
    drone = Drone(i, 30, vision_field_degrees,cap)
    drones.append(drone)"""
###############################################################