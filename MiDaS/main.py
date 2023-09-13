from initialize_variables import *
from delete_files_in_folder import delete_files_in_folder
import multiprocessing
from capture_and_analyze_video import capture_and_analyze_video
import time


def main():

    #clean previous screenshtots
    delete_files_in_folder("MiDaS/video_frames")

    #to show frames together
    #frames_list=[]

    manager = multiprocessing.Manager()
    frames_list = manager.list()

    #better asigment of resources, not all drones are running in parallel
    sleep_times=[]

    #in the first case, do not sleep
    sleep_times.append(0)

    #-1 because the first was asigned
    for i in range(num_drones-1):
        sleep_times.append(i*(interval_seconds/num_drones))


    #define one process for every instance of the dron
    processes = []
    for drone in drones:
        #create process to capture image
        process = multiprocessing.Process(target=capture_and_analyze_video, args=[drone,frames_list,num_drones,sleep_times[drone.id]])
        processes.append(process)
        process.start()

    
    # Wait for all processes to finish
    for process in processes:
        process.join()

    

if __name__ == '__main__': 
    main()
#delete_files_in_folder("MiDaS/video_frames")

