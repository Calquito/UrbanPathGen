import numpy as np
from scipy import ndimage

def identify_routes(depth_area,min_adjacent_elements):

    # Etiquetar los componentes conectados
    labeled_components, num_components = ndimage.label(depth_area)

    # Calcular el tamaño de cada componente
    sizes = np.bincount(labeled_components.ravel())[1:]

    # Filtrar las áreas por tamaño mínimo
    filtered_areas = [i+1 for i, tamano in enumerate(sizes) if tamano >= min_adjacent_elements]

    # Crear una matriz binaria con las áreas filtradas
    filtered_matrix = np.isin(labeled_components, filtered_areas).astype(int)

    return filtered_matrix