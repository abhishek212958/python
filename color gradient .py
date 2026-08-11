import cv2
import numpy as np

width = 600
height = 400

img = np.zeros((height, width, 3), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        blue = x * 255 // width
        green = y * 255 // height
        red = 255 - blue

        img[y, x] = (blue, green, red)

cv2.imshow("RGB Gradient", img)
cv2.waitKey(0)
cv2.destroyAllWindows()