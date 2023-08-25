import cv2
import numpy as np

watermelon = cv2.imread("resources/watermelon.jpg")
materwelon = watermelon.copy()

R,C,Z = watermelon.shape

for r in range(R):
    for c in range(C):
        materwelon[r,c,1], materwelon[r,c,2] = materwelon[r,c,2], materwelon[r,c,1]


resized_watermelon = cv2.resize(watermelon, None, fx=0.3, fy=0.3)
resized_materwelon = cv2.resize(materwelon, None, fx=0.3, fy=0.3)

cv2.imshow("watermelon", resized_watermelon)
cv2.imshow("materwelon", resized_materwelon)
cv2.waitKey()
cv2.imwrite("outputs/materwelon.jpg", materwelon)




