import cv2
import time

def capture_frames_and_show_video(video_path, frequency):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("No se pudo abrir el video.")
        return
    
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    video_duration = frame_count / frame_rate
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    interval_seconds = frequency
    frame_counter = 0
    screenshot_counter=0
    last_screenshot_time = time.time()
    video_start_time=time.time()
    
    while True:
        success, frame = cap.read()
        
        if success:
            frame_counter += 1
            current_time = time.time()
            if current_time - last_screenshot_time >= interval_seconds:
                screenshot_filename = f"MiDaS/video_frames/screenshot_{screenshot_counter}.png"
                cv2.imwrite(screenshot_filename, frame)
                print(f"Captura de pantalla guardada: {screenshot_filename}")
                last_screenshot_time = time.time()
                screenshot_counter+=1
            
            cv2.imshow("Video", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        time.sleep(0.01)
    
    cap.release()
    cv2.destroyAllWindows()

# Ejemplo de uso
video_path = "MiDaS/test_video/aa.webm"
frequency = 5  # Capturar una captura de pantalla cada 5 segundos
capture_frames_and_show_video(video_path, frequency)


while True:
    print("hello")
    paralell_function()