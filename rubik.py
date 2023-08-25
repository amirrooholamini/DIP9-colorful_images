import cv2
import numpy as np
image = cv2.imread("resources/rubik.png")

R,C,Z = image.shape
print(R,C,Z)

color_to_replace = np.array([255, 0, 0])
replacement_color = np.array([0, 255, 255])
pixels_to_replace = np.all(image == color_to_replace, axis=-1)
image[pixels_to_replace] = replacement_color

color_to_replace = np.array([255, 255, 0])
replacement_color = np.array([0, 0, 255])
pixels_to_replace = np.all(image == color_to_replace, axis=-1)
image[pixels_to_replace] = replacement_color

color_to_replace = np.array([0, 255, 0])
replacement_color = np.array([255, 0, 255])
pixels_to_replace = np.all(image == color_to_replace, axis=-1)
image[pixels_to_replace] = replacement_color

cv2.imshow("solved", image)
cv2.waitKey()

cv2.imwrite("outputs/rubik_solved.jpg", image)