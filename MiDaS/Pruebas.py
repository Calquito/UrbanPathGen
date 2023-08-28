import cv2
import threading
import queue

def thread_function(queue):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        queue.put(frame)
    cap.release()

frame_queue = queue.Queue()

# Create and start the thread
thread = threading.Thread(target=thread_function, args=(frame_queue,))
thread.start()

while True:
    if not frame_queue.empty():
        frame = frame_queue.get()
        cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

thread.join()
cv2.destroyAllWindows()