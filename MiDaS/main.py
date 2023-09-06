from initialize_variables import *
from delete_files_in_folder import delete_files_in_folder
import multiprocessing
from capture_and_analyze_video import capture_and_analyze_video


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

