#HARDWARE DEPENDENT###########################################

#vision field of the dron camera
vision_field_degrees=180

#turning accuracy
accuracy=10
#################################################################

#name of the image to read
filename= "Midas\\imagenes_de_prueba\\g.jpeg"


#number of submatrices
submatrices=vision_field_degrees//accuracy

#percentaje of the image considererd
image_percentage=50

#threshold fraction
threshold_fraction=0.4

#model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)