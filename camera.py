import cv2

def takeimage():
    cam = cv2.VideoCapture(0)

    result, image = cam.read()

    cv2.imwrite("capture.png", image) 
  
  
 
   