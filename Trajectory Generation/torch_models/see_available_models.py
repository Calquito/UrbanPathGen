import torch

# Specify the repository name
#repository = 'intel-isl/MiDaS'

repository='"intel-isl/MiDaS", "transforms"'

# List the available models for the specified repository
models_list = torch.hub.list(repository)

# Print the list of available models
print(models_list)

#['DPTDepthModel', 'DPT_BEiT_B_384', 'DPT_BEiT_L_384', 'DPT_BEiT_L_512', 'DPT_Hybrid', 'DPT_Large', 'DPT_LeViT_224', 
# 'DPT_Next_ViT_L_384', 'DPT_SwinV2_B_384', 'DPT_SwinV2_L_384', 'DPT_SwinV2_T_256', 'DPT_Swin_L_384', 'MiDaS', 
# 'MiDaS_small', 'MidasNet', 'MidasNet_small', 'transforms'] 