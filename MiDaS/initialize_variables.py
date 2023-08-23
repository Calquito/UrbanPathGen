import cv2
import time
from drone import Drone
from load_model import load_model

#HARDWARE DEPENDENT###########################################

#vision field of the dron camera
vision_field_degrees=180

#turning accuracy
accuracy=10

#number of drones
num_drones=3
#################################################################

#Video variables#################################################
video_path='MiDaS/test_video/aa.webm'

cap = cv2.VideoCapture(video_path)

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
video_duration = frame_count / frame_rate
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))


interval_seconds = 4

###############################################################
#name of the image to read
original_image= "Midas\\imagenes_de_prueba\\ff.jpeg"


#number of submatrices
submatrices=vision_field_degrees//accuracy

#percentaje of the image considererd
image_percentage=50

#threshold fraction
threshold_fraction=0.25

frecuency_of_images=3

#model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

#Variables for complete analysis###############################
#load de MiDaS model to be used
transform,device,midas=load_model(model_type)

# Create a list to store drones
drones = []

for i in range(num_drones):
    drone = Drone(i, 30, vision_field_degrees)
    drones.append(drone)
###############################################################