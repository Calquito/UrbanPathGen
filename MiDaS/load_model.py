import torch
import warnings

#working non default combinations
#MODEL      TRANSFORM
#Midas      default_transform

#torch.hub.load throws a warning that says that the model is migrated, so it is not needed to do anything
def load_migrated_model(model_type):
    midas = torch.hub.load("intel-isl/MiDaS", model_type)
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    midas.to(device)
    midas.eval()

    midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

    transform = midas_transforms.small_transform

    """
    if model_type == "DPT_Large" or model_type == "DPT_Hybrid" or model_type == "MiDaS":
        print("Using dpt transform")
        transform = midas_transforms.dpt_transform
    else:
        print("Using small transforms")
        transform = midas_transforms.small_transform"""
    
    return transform,device,midas

def load_model(model_type):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return load_migrated_model(model_type)
        