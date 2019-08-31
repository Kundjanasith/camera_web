import cv2
vidcap = cv2.VideoCapture('https://192.168.2.1:5000/video_feed')
success,image = vidcap.read()
count = 0
while success:
    cv2.imwrite("frame%d.jpg" % count, image) # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
