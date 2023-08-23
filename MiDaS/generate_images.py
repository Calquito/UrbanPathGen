import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image
import matplotlib.cm as cm
import os

def delete_files_in_folder(folder_path):
    try:
        # Get list of files in folder
        files = os.listdir(folder_path)

        for file in files:
            file_path = os.path.join(folder_path, file)
            
            # Check if is file (no directory)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except Exception as e:
        print(f"Error deleting files: {e}")

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


def save_plot(input_matrix, filename):
    np.set_printoptions(threshold=sys.maxsize, suppress=True)
    cmap = plt.cm.jet
    plt.axis('off')  
    plt.imshow(input_matrix, cmap=cmap)

    # Save the image in the specified file
    plt.savefig(filename,bbox_inches='tight', pad_inches=0,dpi=300)
"""
def save_plot(input_matrix, filename):
    # Apply 'jet' colormap to the input_matrix
    colormap = cm.get_cmap('jet')
    rgba_matrix = colormap(input_matrix) * 255
    rgba_matrix = rgba_matrix.astype(np.uint8)

    # Create a PIL image from the RGBA array
    image = Image.fromarray(rgba_matrix)

    # Save the image
    image.save(filename)"""


def generate_merged_images(image_matrix_lists,merged_image_name,tmp_folder="MiDaS/tmp_images"):
    tmp_cont=0
    for image in image_matrix_lists:
        save_plot(image,tmp_folder+"/"+str(tmp_cont)+".png")
        tmp_cont+=1
    image_paths=[]
    for i in range(tmp_cont):
        image_paths.append(tmp_folder+"/"+str(i)+".png")
    merge_images(image_paths,merged_image_name)
    delete_files_in_folder(tmp_folder)
    