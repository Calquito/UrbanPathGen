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
