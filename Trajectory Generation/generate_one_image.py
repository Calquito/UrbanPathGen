from complete_analysis import complete_analysis
from generate_images import generate_merged_images
from load_model import load_model
import cv2
from UAV import UAV

#used to test the routes selection algorithm with one image

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
take_screenshots=False

#threshold of depth to be considered a route
threshold_fraction=0.25


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

drone=UAV(2,0.5,field_of_view_x,field_of_view_y,min_vertical_height,max_vertical_height,1.5,resolution_x,resolution_y,'Trajectory Generation/test_video/woods.mp4','video')


#number of submatrices
submatrices=drone.field_of_view_x//accuracy

#TEST ONE IMAGE####################################################################################

#path of the image
image_path='Trajectory Generation\\test_images\\city_door.jpg'
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#load de MiDaS model to be used
transform,device,midas=load_model(model_type)


#do the analyis
depth_area, depth_estimation_matrix=complete_analysis(drone,image,transform,device,midas,threshold_fraction,submatrices,interval_seconds)

#generate the results
generate_merged_images([image,depth_estimation_matrix,depth_area],'Trajectory Generation/image_analysis/output.png')