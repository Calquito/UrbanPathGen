import torch

#working non default combinations
#MODEL      TRANSFORM
#Midas      default_transform
def load_model(model_type):
    midas = torch.hub.load("intel-isl/MiDaS", model_type)
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    midas.to(device)
    midas.eval()

    midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

    transform = midas_transforms.small_transform

    """
    if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
        print("Using dpt transform")
        transform = midas_transforms.dpt_transform
    #elif model_type == "MiDaS":
     #   transform = midas_transforms.default_transform
    else:
        print("Using small transforms")
        transform = midas_transforms.small_transform"""
    
    return transform,device,midas