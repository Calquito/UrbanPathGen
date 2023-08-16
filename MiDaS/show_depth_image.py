import numpy as np
import matplotlib.pyplot as plt
import sys

def show_depth_image(output):
    #show deepth analysis
    np.set_printoptions(threshold=sys.maxsize,suppress = True)
    cmap = plt.cm.jet
    plt.imshow(output,cmap=cmap)

    a = np.array(output)
    mat = np.matrix(a)

    """
    with open('MiDaS/outfile.txt','wb') as f:
        for line in mat:
            np.savetxt(f, line, fmt='%.2f')"""

    plt.show()

