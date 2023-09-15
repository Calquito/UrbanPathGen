from initialize_variables import *
from complete_analysis import complete_analysis
from delete_files_in_folder import delete_files_in_folder
import time
import torch.nn.functional as F
import cv2
import threading
import keyboard
import multiprocessing

def show_current_frame_in_video(frames_list):
    resized_frames_list=[]
    for frame in frames_list:
        new_width = 320
        new_height = 240
        resized_frame = cv2.resize(frame, (new_width, new_height))
        resized_frames_list.append(resized_frame)

    resultado = cv2.hconcat(resized_frames_list)
    cv2.imshow('Video', resultado)


def capture_and_analyze_video(drone,frames_list,num_drones,before_cicle_sleep_time,interval_seconds,take_screenshots,dron_to_show):
    ##video
    cap = cv2.VideoCapture(drone.video_source)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    video_duration = frame_count / frame_rate

    success, frame = cap.read()
    frames_list.append(frame)

    #wait for first frame of all drones

    while(len(frames_list)<num_drones):
        time.sleep(1)

    time.sleep(before_cicle_sleep_time)

    ######################################3
    last_screenshot_time = time.time()
    screenshot_counter=0

    if(show_video and take_screenshots and drone.id==dron_to_show):
        print("Drone "+str(drone.id)+" is displaying video type "+drone.video_type+" and taking screenshots")
         #reads the video
        while True:
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(interval_seconds * frame_rate))
            success, frame = cap.read()
            frames_list[drone.id]=frame
            #frame=cv2.resize(frame, (681,384))
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    #take screenshots of the frames
                    screenshot_filename = f"MiDaS/video_frames/screenshot_{screenshot_counter}_drone{drone.id}.png"
                    cv2.imwrite(screenshot_filename, frame)

                    last_screenshot_time = time.time()
                    screenshot_counter+=1
                    thread = threading.Thread(target=complete_analysis,args=(drone,frame,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees))
                    thread.start()


                show_current_frame_in_video(frames_list)
            else:
                break


            time.sleep(between_frame_sleep_time)
        
        cap.release()
        cv2.destroyAllWindows()

    elif(show_video and take_screenshots and not drone.id==dron_to_show):
        print("Drone "+str(drone.id)+" is displaying video type "+drone.video_type+" and taking screenshots")
         #reads the video
        while True:
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(interval_seconds * frame_rate))
            success, frame = cap.read()
            frames_list[drone.id]=frame
            #frame=cv2.resize(frame, (681,384))
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    #take screenshots of the frames
                    screenshot_filename = f"MiDaS/video_frames/screenshot_{screenshot_counter}_drone{drone.id}.png"
                    cv2.imwrite(screenshot_filename, frame)

                    last_screenshot_time = time.time()
                    screenshot_counter+=1
                    thread = threading.Thread(target=complete_analysis,args=(drone,frame,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees))
                    thread.start()


                time.sleep(0.01)

            else:
                break


            time.sleep(between_frame_sleep_time)
        
        cap.release()
        cv2.destroyAllWindows()

    elif(show_video and not take_screenshots and drone.id==dron_to_show):
        print("Drone "+str(drone.id)+" is displaying video type "+drone.video_type+" and not taking screenshots")
         #reads the video
        while True:
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(interval_seconds * frame_rate))
            success, frame = cap.read()
            frames_list[drone.id]=frame
            #frame=cv2.resize(frame, (681,384))
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:

                    last_screenshot_time = time.time()
                    screenshot_counter+=1
                    thread = threading.Thread(target=complete_analysis,args=(drone,frame,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees))
                    thread.start()


                show_current_frame_in_video(frames_list)

            else:
                break


            time.sleep(between_frame_sleep_time)
        
        cap.release()
        cv2.destroyAllWindows()

    elif(show_video and not take_screenshots and not drone.id==dron_to_show):
        print("Drone "+str(drone.id)+" is displaying video type "+drone.video_type+" and not taking screenshots")
         #reads the video
        while True:
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(interval_seconds * frame_rate))
            success, frame = cap.read()
            frames_list[drone.id]=frame
            #frame=cv2.resize(frame, (681,384))
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:

                    last_screenshot_time = time.time()
                    screenshot_counter+=1
                    thread = threading.Thread(target=complete_analysis,args=(drone,frame,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees))
                    thread.start()

                time.sleep(0.01)
            else:
                break


            time.sleep(between_frame_sleep_time)
        
        cap.release()
        cv2.destroyAllWindows()


    elif(drone.video_type=='video' and take_screenshots):
        print("Drone "+str(drone.id)+" is reading video"+" and taking screenshots")
        while True:
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(screenshot_counter*interval_seconds * frame_rate))
            success, frame = cap.read()
            #frame=cv2.resize(frame, (681,384))
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    #take screenshots of the frames
                    screenshot_filename = f"MiDaS/video_frames/screenshot_{screenshot_counter}_drone{drone.id}.png"
                    cv2.imwrite(screenshot_filename, frame)

                    last_screenshot_time = time.time()
                    screenshot_counter+=1
                    thread = threading.Thread(target=complete_analysis,args=(drone,frame,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees))
                    thread.start()

            else:
                break


            time.sleep(between_frame_sleep_time)
        
        cap.release()
        cv2.destroyAllWindows()

    elif(drone.video_type=='video' and not take_screenshots):
        print("Drone "+str(drone.id)+" is reading video"+" and not taking screenshots")
        while True:
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(screenshot_counter*interval_seconds * frame_rate))
            success, frame = cap.read()
            #frame=cv2.resize(frame, (681,384))
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    last_screenshot_time = time.time()
                    screenshot_counter+=1
                    thread = threading.Thread(target=complete_analysis,args=(drone,frame,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees))
                    thread.start()

            else:
                break


            time.sleep(between_frame_sleep_time)
        
        cap.release()
        cv2.destroyAllWindows()

    #reading from camera, doesnt need to keep taking frames, that means it doesnt need the threads

    elif(drone.video_type=='camera' and  take_screenshots):
        print("Drone "+str(drone.id)+" is reading camera"+" and taking screenshots")
        while True:
            success, frame = cap.read()
            #frame=cv2.resize(frame, (681,384))
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    #take screenshots of the frames
                    screenshot_filename = f"MiDaS/video_frames/screenshot_{screenshot_counter}_drone_{drone.id}.png"
                    cv2.imwrite(screenshot_filename, frame)

                    last_screenshot_time = time.time()
                    screenshot_counter+=1                    
                    complete_analysis(drone,frame,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees)
            else:
                break
        
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Drone "+str(drone.id)+" is reading camera"+" and not taking screenshots")
        while True:
            success, frame = cap.read()
            #frame=cv2.resize(frame, (681,384))
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    last_screenshot_time = time.time()
                    screenshot_counter+=1                    
                    complete_analysis(drone,frame,transform,device,midas,threshold_fraction,image_percentage,submatrices,vision_field_degrees)
            else:
                break
        
        cap.release()
        cv2.destroyAllWindows()
        



