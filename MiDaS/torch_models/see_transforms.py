import torch

# Load the transforms module from "intel-isl/MiDaS"
midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

# List the available transforms
available_transforms = dir(midas_transforms)

# Print the list of available transforms
print(available_transforms)

#['NormalizeImage', 'PrepareForNet', 'Resize', '__builtins__', '__cached__', 
# '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
# 'apply_min_size', 'beit512_transform', 'cv2', 'default_transform', 'dpt_transform', 
# 'levit_transform', 'math', 'np', 'small_transform', 'swin256_transform', 'swin384_transform']