import cv2
import numpy
image = cv2.imread("resources/mohsen.jpg")

R, C , Z = image.shape

gray_image = numpy.zeros((R,C))
for r in range(R):
    for c in range(C):
        gray_image[r,c] = (gray_image[r,c] + image[r,c,0] + image[r,c,1] + image[r,c,2])/3

gray_image = gray_image.astype(numpy.uint8)

cv2.imwrite("outputs/mohsen_gray.jpg", gray_image)


