import torch
import warnings

#working non default combinations

#torch.hub.load throws a warning that says that the model is migrated, so it is not needed to do anything
def load_migrated_model(model_type):
    #load model with pytorch
    midas = torch.hub.load("intel-isl/MiDaS", model_type)
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    midas.to(device)
    midas.eval()
    midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
    transform = midas_transforms.small_transform

    #dpt_transform takes too long and is not necessary if resolution isn't high
    """
    if model_type == "DPT_Large" or model_type == "DPT_Hybrid" or model_type == "MiDaS":
        print("Using dpt transform")
        transform = midas_transforms.dpt_transform
    else:
        print("Using small transforms")
        transform = midas_transforms.small_transform"""
    
    return transform,device,midas

#loads the MiDaS model to use in the execution
def load_model(model_type):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return load_migrated_model(model_type)
        