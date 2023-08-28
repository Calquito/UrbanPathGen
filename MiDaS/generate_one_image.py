from complete_analysis import complete_analysis
from generate_images import generate_merged_images
import numpy as np
from PIL import Image
from initialize_variables import *


image='Midas\\imagenes_de_prueba\\puertas_casa.jpeg'
depth_area, depth_estimation_matrix,bounded_matrix=complete_analysis(drones[0],image,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees)
generate_merged_images([np.array(Image.open(image)),depth_estimation_matrix,depth_area],'MiDaS/image_analysis/output.png')