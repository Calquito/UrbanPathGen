from initialize_variables import *
from complete_analysis import complete_analysis

from scipy import ndimage
import torch
import time
import numpy as np
import torch.nn.functional as F
import cv2
import threading
import multiprocessing


def main():
    last_screenshot_time = time.time()
    video_start_time=time.time()
    
    frame_counter = 0
    screenshot_counter=0

    #reads the video
    while True:
        success, frame = cap.read()
        
        if success:
            frame_counter += 1
            current_time = time.time()

            #take current frame
            if current_time - last_screenshot_time >= interval_seconds:
                screenshot_filename = f"MiDaS/video_frames/screenshot_{screenshot_counter}.png"
                cv2.imwrite(screenshot_filename, frame)
                print(f"Captura de pantalla guardada: {screenshot_filename}")
                last_screenshot_time = time.time()
                screenshot_counter+=1
                thread = threading.Thread(target=complete_analysis,args=(screenshot_filename, f"MiDaS/image_analysis/frame_{screenshot_counter}.png",transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees,num_drones,drones))
                thread.start()
                
            cv2.imshow("Video", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

        time.sleep(0.01)
    
    cap.release()
    cv2.destroyAllWindows()

#main()
complete_analysis(original_image, f"MiDaS/image_analysis/frame_.png",transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees,num_drones,drones)
