#name of the image to read
filename= "Midas\\imagenes_de_prueba\\ss.jpeg"

#vision field of the dron camera
vision_field=180

#turning accuracy
accuracy=10

#number of submatrices
submatrices=vision_field//accuracy


#percentaje of the image considererd
image_percentage=50

model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
#model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)