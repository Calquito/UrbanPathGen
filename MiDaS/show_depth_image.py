import numpy as np
import matplotlib.pyplot as plt
import sys

#show depth estimation using matplotlib
def show_depth_image(output):
    #show deepth analysis
    np.set_printoptions(threshold=sys.maxsize,suppress = True)
    cmap = plt.cm.jet
    plt.imshow(output,cmap=cmap)
    plt.show()

