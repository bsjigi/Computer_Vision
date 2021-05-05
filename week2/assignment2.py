import cv2
import numpy as np

image = cv2.imread('D:/cat.jpg' )

pt = ( -1 , -1)

title = 'assignment2 cat'
cv2 . rectangle ( image , (280 , 130) , (440 , 310) , (0 ,0 ,255) , 2)
cv2 . putText ( image , " cat ", (280 , 130) , cv2 . FONT_HERSHEY_PLAIN , 2, (0 , 0, 255) , thickness =2)

def onMouse ( event , x , y , flags , param ):
    pass


cv2.imshow( title , image )
cv2.setMouseCallback ( title , onMouse )
cv2.waitKey (0)
