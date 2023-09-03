from initialize_variables import *
from complete_analysis import complete_analysis
from delete_files_in_folder import delete_files_in_folder
from scipy import ndimage
import time
import numpy as np
import torch.nn.functional as F
import cv2
import threading
import os
import multiprocessing
import keyboard




def capture_and_analyze_video(drone,num_drones):
    last_screenshot_time = time.time()
    screenshot_counter=0

    #reads the video
    while True:
        success, frame = drone.cap.read()
        
        if success:
            current_time = time.time()
            #take current frame
            if current_time - last_screenshot_time >= interval_seconds:
                #take screenshots of the frames
                screenshot_filename = f"MiDaS/video_frames/screenshot_{screenshot_counter}_drone{drone.id}.png"
                cv2.imwrite(screenshot_filename, frame)

                last_screenshot_time = time.time()
                screenshot_counter+=1

                #pasar reproducción de video a otro thread
                #poner variable si es video o camara


                #complete_analysis(drone,frame,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees)
                thread = threading.Thread(target=complete_analysis,args=(drone,frame,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees))
                thread.start()
                


            
            if(show_video and dron_to_show==drone.id):
                new_width = int(frame.shape[1] * resize_fraction)
                new_height = int(frame.shape[0] * resize_fraction)
                resized_frame = cv2.resize(frame, (new_width, new_height))
                cv2.imshow("Video", resized_frame)

            #use key to kill
            if keyboard.is_pressed("k"):
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break


        time.sleep(0.005)
    
    cap.release()
    cv2.destroyAllWindows()



def main():

    #clean previous screenshtots
    delete_files_in_folder("MiDaS/video_frames")

    #define one thread for every instance of the dron
    threads = []
    for instance in drones:
        thread = threading.Thread(target=capture_and_analyze_video, args=[instance,dron_to_show])
        threads.append(thread)
        thread.start()
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    


main()
#delete_files_in_folder("MiDaS/video_frames")

