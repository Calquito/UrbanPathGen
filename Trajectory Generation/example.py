from UAV import UAV
from trajectory_generation import trajectory_generation

#HARDWARE DEPENDENT################################################################################

#vision field of the dron camera
field_of_view_x=87 #AI-deck color camera module
field_of_view_y=87 #AI-deck color camera module

#turning accuracy degrees
accuracy=5

#resolution of the camera
resolution_x=320
resolution_y=320

#VIDEO VARIABLES###################################################################################

#the frequency at which a frame is captured for analysis
interval_seconds = 1

#shows video taken by the drones (power intensive, may crash the program)
show_video=False

#video resolution can be to big, so to resize it
resize_fraction=0.5

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

#create instances of drones
drones = []
drones.append(UAV(0,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,'Trajectory Generation/test_videos/building.mp4','video'))
drones.append(UAV(1,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,0,'camera'))
drones.append(UAV(2,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,'Trajectory Generation/test_videos/woods.mp4','video'))
drones.append(UAV(3,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,'Trajectory Generation/test_videos/building.mp4','video'))
drones.append(UAV(4,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,'Trajectory Generation/test_videos/building.mp4','video'))
drones.append(UAV(5,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,'Trajectory Generation/test_videos/building.mp4','video'))


#Call trajectory_generation
trajectory_generation(drones,interval_seconds,take_screenshots,model_type,show_video,threshold_fraction,accuracy,print_analysis_time)