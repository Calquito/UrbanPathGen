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
    with open('outfile.txt','wb') as f:
        for line in mat:
            np.savetxt(f, line, fmt='%.2f')"""

    plt.show()



#que porcentaje de la imagen descartar?
#o descartar por áreas contiguas
#requeriría un análisis matricial complejo
