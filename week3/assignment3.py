import cv2
import numpy as np
from numpy.lib import math

theta = math.radians(10)
rot_mat = np . array ([[ np . cos ( theta ) , -np . sin ( theta )],
                        [ np . sin ( theta ) , np . cos ( theta ) ]] , np . float32 )



pts = np . array ([(-150 , -150) , (150 , -150) ,
                    (150 , 150) , (-150 , 150) ], np . float32 )
pts1 = pts



for i in range(1,150):
    globals()['pts{}'.format(i+1)] = cv2 . gemm ( globals()['pts{}'.format(i)] , rot_mat , 1, None, 1, flags = cv2.GEMM_2_T )

#for i , ( pt1 , pt2 ) in enumerate ( zip ( pts1 , pts2 )):
 #   print (" pts1 [%d] = %s, pst2 [%d]= %s" %( i , pt1 , i , pt2 ))

image = np . full ((500 , 500 , 3) , 0 , np . uint8 )#검은색 배경

for i in range(1,150):
    cv2 . polylines ( image , [ np . int32 ( globals()['pts{}'.format(i)] + 250 )] , True , (255 , 255 , 255) , 2)#흰색 선

cv2 . imshow (" assignment3 ", image )
cv2 . waitKey (0)