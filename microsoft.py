import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

microsoft = np.zeros((435,1160,3))
microsoft[:,:] = (82,83,87) 

microsoft[145:215,145:215,:] = (34, 80, 242)
microsoft[145:215,220:290,:] = (0, 186 , 127)
microsoft[220:290,145:215,:] = (239, 164, 0)
microsoft[220:290,220:290,:] = (0, 185 , 255)

microsoft = microsoft.astype(np.uint8)
pil_image = Image.fromarray(microsoft)
font_path = 'fonts/segoeuib.ttf'
font = ImageFont.truetype(font_path, size=150)
draw = ImageDraw.Draw(pil_image)
text = "Microsoft"
position = (300, 110)
font_color = (255, 255, 255)
draw.text(position, text, font=font, fill=font_color)
result_image = np.array(pil_image)

# microsoft = microsoft.astype(np.uint8)
cv2.imshow("microsoft", result_image)
cv2.waitKey()

cv2.imwrite("outputs/microsoft1.jpg", result_image)