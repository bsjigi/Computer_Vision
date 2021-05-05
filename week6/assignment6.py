import numpy as np
import cv2

gaussianfilter = np . array ([1 ,2 ,3, 4, 5, 5,3,2 ,1]) # (3 ,)
gaussianfilter = gaussianfilter [: , None ] # (3 , 1)
gaussianfilter = gaussianfilter @ gaussianfilter . T # (3 ,1)@(1 ,3) =(3 ,3)
gaussianfilter = gaussianfilter / np . sum ( gaussianfilter )
gaussianfilter = gaussianfilter [: , : , None ] # (3 , 3, 1) 3x3 5x5

offset = 4
#print(gaussianfilter)
#print(np.sum(gaussianfilter))

#exit()

image = cv2.imread('qqq.jpg')
cv2.imshow('orig', image)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def gflit ( img , oshape ) :
    filterd = np . zeros ( oshape , dtype = np . uint8 )
    for y in range (0 , oshape [0]) :
        for x in range (0 , oshape [0]) :
            filterd [y , x] = np . round ( np . sum ( img [y:y +2* offset +1 , 
            x:x +2* offset +1]* gaussianfilter , axis =0) .sum( axis =0) )
    return filterd

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 2)

    ih, iw, _ = img.shape

    for (x,y,w,h) in faces:
        newy1 = y-offset
        newy2 = y+h+offset
        newx1 = x-offset
        newx2 = x+w+offset

        pady1 = -min(newy1, 0)
        padx1 = -min(newx1, 0)
        pady2 = max(newy2-ih, 0)
        padx2 = max(newy2-ih, 0)

        imgf = img[max(newy1, 0):newy2, max(newx1, 0):newx2].copy()
        imgf = np.pad(imgf, ((pady1, pady2), (padx1,padx2), (0,0)), 'reflect')

        #cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        img[y:y+h, x:x+w] = gflit(imgf, img[y:y+h, x:x+w].shape)

detect_face(image)

cv2.imshow('filtered', image)

cv2.waitKey(0)

