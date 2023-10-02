from complete_analysis import complete_analysis
import time
import cv2
import threading


#show video using cv2. Can slow the program
def show_current_frame_in_video(frames_list):
    resized_frames_list=[]
    for frame in frames_list:
        new_width = 320
        new_height = 240
        resized_frame = cv2.resize(frame, (new_width, new_height))
        resized_frames_list.append(resized_frame)

    resultado = cv2.hconcat(resized_frames_list)
    cv2.imshow('Video', resultado)


#capture the images for the analysis 
def capture_and_analyze_video(drone,frames_list,num_drones,before_cicle_sleep_time,interval_seconds,take_screenshots,dron_to_show,show_video,threshold_fraction,transform,device,midas,accuracy):        
    #capture video
    cap = cv2.VideoCapture(drone.video_source)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

    #starts reading the flux of video
    success, frame = cap.read()
    frames_list.append(frame)

    #wait for all drones to be loaded before starting the execution
    while(len(frames_list)<num_drones):
        time.sleep(1)
    time.sleep(before_cicle_sleep_time)

    #number of submatrices
    submatrices=drone.field_of_view_x//accuracy

    between_frame_sleep_time=0.2

    #defines the time since the last capture
    last_screenshot_time = time.time()

    screenshot_counter=0


    #dekay time between frames, so video doesn't go to fast
    between_frame_sleep_time_with_video=0.01
    
    #select option depending on show_video, take_screenshots and the dron whose process show the video
    #OPTIONS ARE SIMILAR BUT NOT EQUAL, SO REPEATED CHARACTERISTICS ARE DEFINED ONCE 
    if(show_video and take_screenshots and drone.id==dron_to_show):
        #displays the option
        print("Drone "+str(drone.id)+" is displaying video type "+drone.video_type+" and taking screenshots")
        #reads the video while exists (the process)
        while True:
            #read the frame and add it to the list of shared frames
            success, frame = cap.read()
            frames_list[drone.id]=frame
            
            #if it could read the frame (frame exists)
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    #take screenshots of the frames
                    screenshot_filename = f"Trajectory Generation/video_frames/screenshot_{screenshot_counter}_drone_{drone.id}.png"
                    cv2.imwrite(screenshot_filename, frame)

                    #update time since last screenshot
                    last_screenshot_time = time.time()
                    screenshot_counter+=1

                    #start the thread that makes the analysis of the image
                    thread=threading.Thread(target=complete_analysis,args=(drone,frame,transform,device,midas,threshold_fraction,submatrices,interval_seconds))
                    thread.start()
    
                time.sleep(between_frame_sleep_time_with_video*0.7)

                #show the current frame in the video
                show_current_frame_in_video(frames_list)
            else:
                break
        
        cap.release()
        cv2.destroyAllWindows()

    elif(show_video and take_screenshots and not drone.id==dron_to_show):
        print("Drone "+str(drone.id)+" is displaying video type "+drone.video_type+" and taking screenshots")
         #reads the video
        while True:
            success, frame = cap.read()
            frames_list[drone.id]=frame
            
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    #take screenshots of the frames
                    screenshot_filename = f"Trajectory Generation/video_frames/screenshot_{screenshot_counter}_drone_{drone.id}.png"
                    cv2.imwrite(screenshot_filename, frame)

                    last_screenshot_time = time.time()
                    screenshot_counter+=1
                    thread=threading.Thread(target=complete_analysis,args=(drone,frame,transform,device,midas,threshold_fraction,submatrices,interval_seconds))
                    thread.start()
    
                time.sleep(between_frame_sleep_time_with_video)

            else:
                break
            
        cap.release()
        cv2.destroyAllWindows()

    elif(show_video and not take_screenshots and drone.id==dron_to_show):
        print("Drone "+str(drone.id)+" is displaying video type "+drone.video_type+" and not taking screenshots")
         #reads the video
        while True:
            success, frame = cap.read()
            frames_list[drone.id]=frame
            
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:

                    last_screenshot_time = time.time()
                    screenshot_counter+=1
                    thread=threading.Thread(target=complete_analysis,args=(drone,frame,transform,device,midas,threshold_fraction,submatrices,interval_seconds))
                    thread.start()
    
                time.sleep(between_frame_sleep_time_with_video*0.7)

                show_current_frame_in_video(frames_list)

            else:
                break
        
        cap.release()
        cv2.destroyAllWindows()

    elif(show_video and not take_screenshots and not drone.id==dron_to_show):
        print("Drone "+str(drone.id)+" is displaying video type "+drone.video_type+" and not taking screenshots")
         #reads the video
        while True:
            success, frame = cap.read()
            frames_list[drone.id]=frame
            
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:

                    last_screenshot_time = time.time()
                    screenshot_counter+=1
                    thread=threading.Thread(target=complete_analysis,args=(drone,frame,transform,device,midas,threshold_fraction,submatrices,interval_seconds))
                    thread.start()
    
                time.sleep(between_frame_sleep_time_with_video)
            else:
                break
        
        cap.release()
        cv2.destroyAllWindows()


    elif(drone.video_type=='video' and take_screenshots):
        print("Drone "+str(drone.id)+" is reading video"+" and taking screenshots")
        while True:
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(screenshot_counter*interval_seconds * frame_rate))
            success, frame = cap.read()
            
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    #take screenshots of the frames
                    screenshot_filename = f"Trajectory Generation/video_frames/screenshot_{screenshot_counter}_drone_{drone.id}.png"
                    cv2.imwrite(screenshot_filename, frame)

                    last_screenshot_time = time.time()
                    screenshot_counter+=1
                    complete_analysis(drone,frame,transform,device,midas,threshold_fraction,submatrices,interval_seconds)

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
            
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    last_screenshot_time = time.time()
                    screenshot_counter+=1
                    complete_analysis(drone,frame,transform,device,midas,threshold_fraction,submatrices,interval_seconds)

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
            
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    #take screenshots of the frames
                    screenshot_filename = f"Trajectory Generation/video_frames/screenshot_{screenshot_counter}_drone_{drone.id}.png"
                    cv2.imwrite(screenshot_filename, frame)

                    last_screenshot_time = time.time()
                    screenshot_counter+=1      

                    #is not displaying video, so there is no need for the thread              
                    complete_analysis(drone,frame,transform,device,midas,threshold_fraction,submatrices,interval_seconds)
            else:
                break
        
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Drone "+str(drone.id)+" is reading camera"+" and not taking screenshots")
        while True:
            success, frame = cap.read()
            
            if success:
                current_time = time.time()
                #take current frame
                if current_time - last_screenshot_time >= interval_seconds:
                    last_screenshot_time = time.time()
                    screenshot_counter+=1                    
                    complete_analysis(drone,frame,transform,device,midas,threshold_fraction,submatrices,interval_seconds)
            else:
                break
        
        cap.release()
        cv2.destroyAllWindows()
        



