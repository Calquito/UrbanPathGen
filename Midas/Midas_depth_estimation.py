import cv2
import torch
import urllib.request

import matplotlib.pyplot as plt
import sys
import numpy as np


#acepta np.array
def split_matrix_vertical(matriz):
    # Obtener el número de columnas de la matriz
    num_columnas = matriz.shape[1]
    
    # Dividir la matriz verticalmente en dos
    parte1 = matriz[:, :num_columnas // 2]
    parte2 = matriz[:, num_columnas // 2:]
    
    # Convertir cada parte en un array
    array_parte1 = parte1.flatten()
    array_parte2 = parte2.flatten()
    
    return array_parte1, array_parte2

#para que la matriz sea multiplo de la cantidad de grados seleccionados
def remove_extra_columns(matrix, multiple):
    original_columns = matrix.shape[1]
    required_columns = (original_columns // multiple) * multiple
    
    if required_columns < original_columns:
        return matrix[:, :required_columns]
    else:
        return matrix
    
#mantener el porcentaje indicado
def select_center_rows(matrix, percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100.")
    
    num_rows = matrix.shape[0]
    num_center_rows = int(num_rows * (percentage / 100))
    start_row = (num_rows - num_center_rows) // 2
    end_row = start_row + num_center_rows
    
    return matrix[start_row:end_row, :], start_row

#divide the matrix in submatrices, do the sum of values, and return y,x coordinates of the first element
#of the matrix with the lower sum

def find_min_sum_submatrix(matrix, N):
    rows, cols = matrix.shape
    num_submatrices_rows = rows // N
    num_submatrices_cols = cols // N
    
    min_sum = float('inf')
    min_row, min_col = None, None
    
    for i in range(num_submatrices_rows):
        for j in range(num_submatrices_cols):
            submatrix = matrix[i*N : (i+1)*N, j*N : (j+1)*N]
            submatrix_sum = np.sum(submatrix)
            
            if submatrix_sum < min_sum:
                min_sum = submatrix_sum
                min_row, min_col = i*N, j*N
    
    return min_row, min_col

########################################################################################################

#url, filename = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg", "dog.jpg")
#urllib.request.urlretrieve(url, filename)

filename= "Midas\\imagenes_de_prueba\\h.jpeg"


model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
#model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

midas = torch.hub.load("intel-isl/MiDaS", model_type)

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
midas.to(device)
midas.eval()

midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = midas_transforms.dpt_transform
else:
    transform = midas_transforms.small_transform

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

input_batch = transform(img).to(device)

with torch.no_grad():
    prediction = midas(input_batch)

    prediction = torch.nn.functional.interpolate(
        prediction.unsqueeze(1),
        size=img.shape[:2],
        mode="bicubic",
        align_corners=False,
    ).squeeze()

output = prediction.cpu().numpy()


###########################################################################################




# Binary decision
"""
# Decide whether to turn left or right
left, right = split_matrix_vertical(output)


# Should choose the deepest position with the smallest number
if sum(left) > sum(right):
    print("Turn right")
else:
    print("Turn left")
"""

# Decision with angles based on a single pixel
# Goes to the deepest points, althoug it may be not convenient, like corners

# Center of the image
"""
center_x = output.shape[1] // 2

# Returns the indices of the point with the smallest value
deepest_point_y, deepest_point_x = np.unravel_index(np.argmin(a), a.shape)

# Distance between points
distance = deepest_point_x - center_x 

print("dpx: "+ str(deepest_point_x))
print("dpy: "+ str(deepest_point_y))
print("center: "+str(center_x))

print("distance: "+str(distance))
#angle, the center is the zero, negative angle is left, positive angle is right

angle=(distance/output.shape[1])*180
print(angle)"""


# Decision with angles based on area

#vision field of the dron camera
vision_field=180

#turning accuracy
accuracy=10

#number of submatrices
submatrices=vision_field//accuracy


#percentaje of the image considererd
image_percentage=50

adjusted_matrix=remove_extra_columns(output,submatrices)

#start_row to sum it in case of needing the y coordinate
bounded_matrix, start_row = select_center_rows(adjusted_matrix,50)

#submatrix NxN dimension
submatrix_dimension=bounded_matrix.shape[1]//submatrices

#get the coordinates of the first element of the deepest submatrix
min_row, min_col=find_min_sum_submatrix(bounded_matrix,submatrix_dimension)

center_x = output.shape[1] // 2


# Distance between points
distance = min_col - center_x 

print("dpx: "+ str(min_col))
print("dpy: "+ str(min_row))
print("center: "+str(center_x))

print("distance: "+str(distance))

#angle, the center is the zero, negative angle is left, positive angle is right

angle=(distance/output.shape[1])*180

print(angle)




np.set_printoptions(threshold=sys.maxsize,suppress = True)
cmap = plt.cm.jet
plt.imshow(output,cmap=cmap)

a = np.array(output)
mat = np.matrix(a)
with open('outfile.txt','wb') as f:
    for line in mat:
        np.savetxt(f, line, fmt='%.2f')

plt.show()





