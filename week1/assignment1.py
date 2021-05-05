import numpy as np
import cv2

image = np . zeros ((400 , 400) , np . uint8 )

image [0:100 , 0:100] = 55
image [0:100 , 100:200] = 155
image [0:100 , 200:300] = 55
image [0:100 , 300:400] = 155

image [100:200 , 0:100] = 155
image [100:200 , 100:200] = 255
image [100:200 , 200:300] = 155
image [100:200 , 300:400] = 255

image [200:300 , 0:100] = 55
image [200:300 , 100:200] = 155
image [200:300 , 200:300] = 55
image [200:300 , 300:400] = 155

image [300:400 , 0:100] = 155
image [300:400 , 100:200] = 255
image [300:400 , 200:300] = 155
image [300:400 , 300:400] = 255



cv2.imshow (" Window title ", image )
cv2.waitKey (0)
cv2.destroyAllWindows ()
