import torch



def estimate_depth(filename,transform,device,midas):

    img=filename
    #img = cv2.imread(filename)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    input_batch = transform(img).to(device)
    retry=4
    cont=0

    while(cont<retry):
        try:
            with torch.no_grad():
                prediction = midas(input_batch) 

                prediction = torch.nn.functional.interpolate(
                    prediction.unsqueeze(1),
                    size=img.shape[:2],
                    mode="bicubic",
                    align_corners=False,
                ).squeeze()
            output = prediction.cpu().numpy()
            break
        except Exception as e:
            print("Fallo"+str(cont))
            cont+=1
            output=[]

    return output








