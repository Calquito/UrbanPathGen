import sys
sys.path.append('Trajectory Generation')

import numpy as np
import pytest
from matrix_analysis import get_middle_horizontal_coordinates

@pytest.mark.parametrize("binary_matrix, min_size, expected_coordinates", [
    (np.array([[1, 1, 1, 1, 1, 1, 0, 1, 0],
               [1, 1, 0, 0, 0, 0, 0, 1, 0],
               [0, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 1, 1, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 1, 0]]), 3, [(1, 2), (5, 2), (4, 5)]),
    (np.array([[1, 1, 1, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 1, 1, 0],
               [1, 0, 1, 1, 1, 1, 1, 1, 0],
               [1, 0, 1, 0, 0, 0, 0, 1, 0]]), 3, [(0, 2), (4, 3)]),
    (np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]), 3, []),
    (np.array([[1, 1, 1, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]), 3, [(1, 1)]),

])
def test_get_middle_horizontal_coordinates(binary_matrix, min_size, expected_coordinates):
    result = get_middle_horizontal_coordinates(binary_matrix, min_size)
    
    assert result == expected_coordinates