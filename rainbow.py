import cv2
import numpy as np

row, col = 600, 1100

result = np.zeros((row,col,3), dtype=np.uint8) + 255

cv2.ellipse(result, (550,450), (300, 300), angle=0, startAngle=0, endAngle=360, color=(0,0,255), thickness=30)
cv2.ellipse(result, (550,450), (270, 270), angle=0, startAngle=0, endAngle=360, color=(0,165,255), thickness=30)
cv2.ellipse(result, (550,450), (240, 240), angle=0, startAngle=0, endAngle=360, color=(0,255,255), thickness=30)
cv2.ellipse(result, (550,450), (210, 210), angle=0, startAngle=0, endAngle=360, color=(0,128,0), thickness=30)
cv2.ellipse(result, (550,450), (190, 190), angle=0, startAngle=0, endAngle=360, color=(255,245,0), thickness=30)
cv2.ellipse(result, (550,450), (160, 160), angle=0, startAngle=0, endAngle=360, color=(255,0,0), thickness=30)
cv2.ellipse(result, (550,450), (130, 130), angle=0, startAngle=0, endAngle=360, color=(128,0,128), thickness=30)

for r in range(450, row):
    result[r,:,:] = 255

cv2.imshow("1",result)
cv2.waitKey()

cv2.imwrite("outputs/rainbow.jpg", result)