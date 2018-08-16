import cv2
import numpy as np

image = cv2.imread("babybears.jpg")
shape = image.shape  # get the shape of the image
print(shape)         # print dem
blue = (255, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)
cv2.line(image, (94, 408), (320, 120), blue, thickness=5)
cv2.circle(image, (250, 250), 50, red, -1)
cv2.rectangle(image, (50, 50,), (150, 150), green, -1)

cv2.imshow("Baby bears", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
