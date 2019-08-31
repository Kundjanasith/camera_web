import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    height, width, channels = frame.shape 
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'@Kundjanasith',(int(width-300),int(height-20)), font, 1,(255,255,255),2,cv2.LINE_AA)
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
