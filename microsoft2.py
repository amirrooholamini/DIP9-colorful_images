import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

microsoft = np.zeros((435,1160,3))
microsoft[:,:] = (230,230,230)

microsoft[0:70,0:70,:] = 210
microsoft[75:145,0:70,:] = 210
microsoft[0:70,75:145,:] = 210
microsoft[75:145,75:145,:] = 210

microsoft[145:215,145:215,:] = (34, 80, 242)
microsoft[145:215,220:290,:] = (0, 186 , 127)
microsoft[220:290,145:215,:] = (239, 164, 0)
microsoft[220:290,220:290,:] = (0, 185 , 255)

microsoft[290:360,0:70,:] = 210
microsoft[365:435,0:70,:] = 210
microsoft[290:360,75:145,:] = 210
microsoft[365:435,75:145,:] = 210

microsoft[0:70,1090:1160,:] = 210
microsoft[0:70,1015:1085,:] = 210
microsoft[75:145,1090:1160,:] = 210
microsoft[75:145,1015:1085,:] = 210

microsoft[290:360,1090:1160,:] = 210
microsoft[290:360,1015:1085,:] = 210
microsoft[365:435,1090:1160,:] = 210
microsoft[365:435,1015:1085,:] = 210

microsoft[145:290,290:1015,:] = 255

microsoft = microsoft.astype(np.uint8)
pil_image = Image.fromarray(microsoft)
font_path = 'fonts/segoeuib.ttf'
font = ImageFont.truetype(font_path, size=150)
draw = ImageDraw.Draw(pil_image)
text = "Microsoft"
position = (300, 110)
font_color = (113, 113, 113)
draw.text(position, text, font=font, fill=font_color)
result_image = np.array(pil_image)

# microsoft = microsoft.astype(np.uint8)
cv2.imshow("1", result_image)
cv2.waitKey()

cv2.imwrite("outputs/microsoft2.jpg", result_image)