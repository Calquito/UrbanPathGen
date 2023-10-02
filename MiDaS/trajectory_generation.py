from delete_files_in_folder import delete_files_in_folder
from capture_and_analyze_video import capture_and_analyze_video
import threading
from load_model import load_model

def trajectory_generation(drones,interval_seconds,take_screenshots,dron_to_show,model_type,show_video,threshold_fraction,submatrices,between_frame_sleep_time):

    
    #clean previous screenshtots
    delete_files_in_folder("MiDaS/video_frames")


    #better asigment of resources, not all drones are running in parallel
    before_cicles_sleep_times=[]

    #in the first case, do not sleep
    before_cicles_sleep_times.append(0)

    #define variables needed to analysis
    num_drones=len(drones)
    frames_list = []

    #-1 because the first was asigned
    for i in range(num_drones-1):
        before_cicles_sleep_times.append(i*(interval_seconds/num_drones))

    #load de MiDaS model to be used
    transform,device,midas=load_model(model_type)


    #define one thread for every instance of the dron
    threads = []
    for drone in drones:
        #create thread to capture image
        thread = threading.Thread(target=capture_and_analyze_video, args=[drone,frames_list,num_drones,before_cicles_sleep_times[drone.id],interval_seconds,take_screenshots,dron_to_show,model_type,show_video,threshold_fraction,submatrices,between_frame_sleep_time,transform,device,midas])
        threads.append(thread)
        thread.start()

    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

#call main from where it's needed
#if __name__ == '__main__':
 #   run()

