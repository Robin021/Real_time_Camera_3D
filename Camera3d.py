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

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use the lower case
# out = cv2.VideoWriter('output3d.mp4', fourcc, 10.0, (width, height))
global i
i = 0 
while(cap.isOpened()):
    cap.set(cv2.CAP_PROP_FPS, 30)
    ret, frame = cap.read()
    if ret == True:
        
        result = img_cartoon(frame)

        frame = np.uint8(result[OutputKeys.OUTPUT_IMG])
        # Draw the Chinese characters on the image using cv2.putText()
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'A-Big-SB'
        cv2.putText(frame, text, (200, 300), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.namedWindow(text, cv2.WINDOW_NORMAL)
        cv2.imshow(text,frame)
        # Set window property to always on top
        cv2.setWindowProperty(text, cv2.WND_PROP_TOPMOST, 2)
        # Change window size
        cv2.resizeWindow(text,500,280)

        if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
            break
    else:
        break

# Release everything if job is finished
out.release()
cap.release()
cv2.destroyAllWindows()
