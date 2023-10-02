from UAV import UAV
from trajectory_generation import trajectory_generation

#HARDWARE DEPENDENT###########################################

#vision field of the dron camera
field_of_view_x=87 #AI-deck color camera module
field_of_view_y=87 #AI-deck color camera module

#turning accuracy degrees
accuracy=5

#resolution of the camera
resolution_x=320
resolution_y=320

#maximum speed of the dron in m/s
max_speed=1


#################################################################

#Video variables#################################################

interval_seconds = 1

show_video=False
take_screenshots=False
analyze_screenshots=False

#video resolution can be to big, so to resize it
resize_fraction=0.5

#dron video to show (dron.id has to exist)
dron_to_show=0

between_frame_sleep_time=0.3

###############################################################
#number of submatrices
submatrices=field_of_view_x//accuracy


#threshold of depth to be considered a route
threshold_fraction=0.25


#models

#model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)#
#model_type = "MiDaS"
#model_type = "transforms"

#Variables for complete analysis###############################



#drones
#min and max vertical height in mts
min_vertical_height=1.0
max_vertical_height=4.0







###############################################################

drones = []
drones.append(UAV(0,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,'MiDaS/test_video/building.mp4','video'))
drones.append(UAV(1,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,0,'camera'))
drones.append(UAV(2,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,'MiDaS/test_video/woods.mp4','video'))
drones.append(UAV(3,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,'MiDaS/test_video/building.mp4','video'))
drones.append(UAV(4,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,'MiDaS/test_video/building.mp4','video'))
drones.append(UAV(5,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,'MiDaS/test_video/building.mp4','video'))


trajectory_generation(drones,interval_seconds,take_screenshots,dron_to_show,model_type,show_video,threshold_fraction,submatrices,between_frame_sleep_time)