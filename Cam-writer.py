import cv2
import sys
cap=cv2.VideoCapture()
vidPath="rtsp://root:pass123@192.168.137.89:554/axis-media/media.amp"
cap.open(vidPath)
count =-1
name=0
skip=10 #Minimum
while(cap.isOpened()):
    ret,frame=cap.read()
    count=count+1
    if count%skip==0:
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #faces= faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
        #for (x,y,w,h) in faces:
        #    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        name=name+1
        filename='Cam/img'+repr(name)+'.jpg'
        cv2.imshow('Video',frame)
        cv2.imwrite(filename,frame)
        if cv2.waitKey(100) & 0xFF== ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()