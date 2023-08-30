from complete_analysis import complete_analysis
from generate_images import generate_merged_images
import numpy as np
from PIL import Image
from initialize_variables import *


filename='MiDaS\\imagenes_de_prueba\\2.jpeg'
image = cv2.imread(filename)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#camera
#depth_area, depth_estimation_matrix,bounded_matrix=complete_analysis(drones[0],drones[0].cap.read()[1],transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees)

#image
depth_area, depth_estimation_matrix,bounded_matrix=complete_analysis(drones[0],image,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees)

generate_merged_images([image,depth_estimation_matrix,depth_area],'MiDaS/image_analysis/output.png')