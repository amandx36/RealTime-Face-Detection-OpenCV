import cv2 as cv

for i in range(3):   # 0, 1, 2 check karenge
    cap = cv.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera {i} available")
        cap.release()
    else:
        print(f"Camera {i} not available")
