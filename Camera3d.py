import numpy as np
import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import numpy as np


# img_cartoon = pipeline(Tasks.image_portrait_stylization,
#                         model='damo/cv_unet_person-image-cartoon-3d_compound-models')

img_cartoon = pipeline(Tasks.image_portrait_stylization,
                      model='damo/cv_unet_person-image-cartoon_compound-models')

cap = cv2.VideoCapture(0) # Capture video from camera
# Get the width and height of frame
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)  + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  + 0.5)
# Create named window with normal flags



# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use the lower case
# out = cv2.VideoWriter('output3d.mp4', fourcc, 10.0, (width, height))
global i
i = 0 
while(cap.isOpened()):
    cap.set(cv2.CAP_PROP_FPS, 30)
    ret, frame = cap.read()
    if ret == True:
        
         
        imagename=str(i)+ "frame.png"
        path="/Users/robin/PycharmProjects/AI_cartoon/tmp/" + imagename
        
        result = img_cartoon(frame)

        frame = np.uint8(result[OutputKeys.OUTPUT_IMG])

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)


        cv2.imshow('frame',frame)

        # Set window property to always on top
        cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)
        # Change window size
        cv2.resizeWindow("frame",400,250)

        # Set window property to always on top
        cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)
        if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
            break
    else:
        break

# Release everything if job is finished
out.release()
cap.release()
cv2.destroyAllWindows()
