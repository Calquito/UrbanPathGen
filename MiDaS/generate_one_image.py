from complete_analysis import complete_analysis
from generate_images import generate_merged_images
import numpy as np
from PIL import Image
from initialize_variables import *
from load_model import load_model
import cv2


#used to test the routes selection algorithm with one image

#path of the image
filename='MiDaS\\imagenes_de_prueba\\forest.jpeg'
image = cv2.imread(filename)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#load de MiDaS model to be used
transform,device,midas=load_model(model_type)

#do the analyis
depth_area, depth_estimation_matrix,bounded_matrix=complete_analysis(drones[2],image,transform,device,midas,threshold_fraction,submatrices,interval_seconds)

#generate the results
generate_merged_images([image,depth_estimation_matrix,depth_area],'MiDaS/image_analysis/output.png')