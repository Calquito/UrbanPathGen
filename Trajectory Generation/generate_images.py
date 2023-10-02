import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image
import matplotlib.cm as cm
import os
from delete_files_in_folder import delete_files_in_folder


#generate images of the original image, the depth estimation plot and the identified routes

def merge_images(image_paths, output_path):
    images = [Image.open(path) for path in image_paths]

    # We assume that all images have the same size.
    image_width, image_height = images[0].size

    # Create a new large image to combine the images.
    total_width = image_width *len(image_paths)  # Change this if you want another number of images per row
    total_height = image_height # We calculate the total height required
    merged_image = Image.new('RGB', (total_width, total_height))

    x_offset = 0
    y_offset = 0

    for image in images:
        # Paste the current image at the current position.
        merged_image.paste(image, (x_offset, y_offset))

        # Update the coordinates for the following image
        x_offset += image_width
        if x_offset >= total_width:
            x_offset = 0
            y_offset += image_height

    merged_image.save(output_path)


#save matplotlib plot
def save_plot(input_matrix, filename):
    np.set_printoptions(threshold=sys.maxsize, suppress=True)
    cmap = plt.cm.jet
    plt.axis('off')  
    plt.imshow(input_matrix, cmap=cmap)

    # Save the image in the specified file
    plt.savefig(filename,bbox_inches='tight', pad_inches=0,dpi=300)


#generate the 3 images together
def generate_merged_images(image_matrix_lists,merged_image_name,tmp_folder="Trajectory Generation/tmp_images"):
    tmp_cont=0
    for image in image_matrix_lists:
        save_plot(image,tmp_folder+"/"+str(tmp_cont)+".png")
        tmp_cont+=1
    image_paths=[]
    for i in range(tmp_cont):
        image_paths.append(tmp_folder+"/"+str(i)+".png")
    merge_images(image_paths,merged_image_name)
    delete_files_in_folder(tmp_folder)
    