from drone import Drone
from load_model import load_model
from math import sqrt, tan, pi


#HARDWARE DEPENDENT###########################################

#vision field of the dron camera
vision_field_degrees=87 #AI-deck color camera module

#turning accuracy degrees
accuracy=5

#resolution of the camera
resolutionx=320
resolutiony=320

#maximum speed of the dron in m/s
max_speed=1


#################################################################

#Video variables#################################################

interval_seconds = 1

show_video=True
take_screenshots=False
analyze_screenshots=False

#video resolution can be to big, so to resize it
resize_fraction=0.5

#dron video to show (dron.id has to exist)
dron_to_show=0

between_frame_sleep_time=0.3

###############################################################
#number of submatrices
submatrices=vision_field_degrees//accuracy

#percentaje of the image considererd
image_percentage=100

#threshold of depth to be considered a route
threshold_fraction=0.25

"""
#estimated height of the area of a route, using sqrt, in pixels
area_height_pixels=sqrt((resolutionx*resolutiony)/submatrices)

#vertical movement estimation###################################
#worse case scenario distance to obstacle. d=v*t
wcs_distance=max_speed*interval_seconds

#worse case scenario height, using trigonometry
#tan uses radians, so convert
alpha=(vision_field_degrees/2)*(pi/180)

#this would be the wsc distance in meters equivalent to the pixels of area_height_pixels
wcs_height=tan(alpha)*wcs_distance

area_height_meters=wcs_height*(area_height_pixels/resolutiony)"""



#models

#model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)#
#model_type = "MiDaS"
#model_type = "transforms"

#Variables for complete analysis###############################



#drones
#min and max vertical height in mts
min_vertical_height=1
max_vertical_height=4

# Create a list to store drones
drones = []

drones.append(Drone(0,0.5,vision_field_degrees,1.0,4.0,1.5,'MiDaS/test_video/building.mp4','video'))
drones.append(Drone(1,0.5,vision_field_degrees,1.0,4.0,1.5,0,'camera'))
drones.append(Drone(2,0.5,vision_field_degrees,1.0,4.0,1.5,'MiDaS/test_video/woods.mp4','video'))
#drones.append(Drone(3,0.5,vision_field_degrees,1.0,4.0,1.5,'MiDaS/test_video/woods.mp4','video'))

num_drones=len(drones)

"""
for i in range(num_drones):
    drone = Drone(i, 30, vision_field_degrees,cap)
    drones.append(drone)"""
###############################################################