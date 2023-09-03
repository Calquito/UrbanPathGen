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



def capture_and_analyze_video(drone,frames_list,num_drones):
    ##video
    cap = cv2.VideoCapture(drone.video_source)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    video_duration = frame_count / frame_rate

    success, frame = cap.read()
    frames_list.append(frame)

    #wait for first frame of all drones

    while(len(frames_list)<num_drones):
        print(len(frames_list))
        time.sleep(1)

    ######################################3
    last_screenshot_time = time.time()
    screenshot_counter=0

    #reads the video
    while True:
        success, frame = cap.read()
        frames_list[drone.id]=frame
        
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
            
            
            if(show_video and drone.id==0):
                resized_frames_list=[]
                for frame in frames_list:
                    new_width = 320
                    new_height = 240
                    resized_frame = cv2.resize(frame, (new_width, new_height))
                    resized_frames_list.append(resized_frame)

                resultado = cv2.hconcat(resized_frames_list)
                cv2.imshow('Video', resultado)
            elif(show_video):
                time.sleep(0.01)

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

    #to show frames together
    #frames_list=[]

    manager = multiprocessing.Manager()
    frames_list = manager.list()

    #define one thread for every instance of the dron
    threads = []
    for drone in drones:
        #create thread to capture image
        thread = multiprocessing.Process(target=capture_and_analyze_video, args=[drone,frames_list,num_drones])
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    

if __name__ == '__main__': 
    main()
#delete_files_in_folder("MiDaS/video_frames")

