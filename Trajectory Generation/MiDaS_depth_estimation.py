import torch


#use MiDaS to estimate depth
def estimate_depth(image,transform,device,midas):

    #uses CUDA if available
    input_batch = transform(image).to(device)

    #if the inference is not possible due to errors, return an empty matrix

    #max number of retrys
    retry=4
    cont=0

    while(cont<retry):
        try:
            #make the prediction
            with torch.no_grad():
                prediction = midas(input_batch) 
                prediction = torch.nn.functional.interpolate(
                    prediction.unsqueeze(1),
                    size=image.shape[:2],
                    mode="bicubic",
                    align_corners=False,
                ).squeeze()
            #depth estimation matrix
            output = prediction.cpu().numpy()
            break
        except Exception as e:
            #print("Error"+str(cont))
            cont+=1
            output=[]

    return output








