import cv2

#/Users/shannenbravo-brown/Desktop/Imaging with python/tutoral1
#Create image
image = cv2.imread("babybears.jpg")
#Gray scale the image
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Shaow regular image
cv2.imshow("Cute Bears", image)
#show gray image
cv2.imshow("Gray Bears", grayImage)
#keep image on screen
cv2.waitKey(0)
#destroy
cv2.destroyAllWindows()