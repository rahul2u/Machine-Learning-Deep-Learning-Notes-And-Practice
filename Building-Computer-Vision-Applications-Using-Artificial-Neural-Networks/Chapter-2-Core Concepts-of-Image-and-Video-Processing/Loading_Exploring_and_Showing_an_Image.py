# import library
import cv2

# image path
image_path = "images/marsrover.png"

# read image
img = cv2.imread(image_path)

# image is numpy array
print(img)

bn  print("Dimensions of Image ", img.ndim)
print("Image Shape", img.shape)
height, width , channels = img.shape
print(height, width, channels)
print("Image Height", img.shape[0])
print("Image Width", img.shape[1])
print("Image Channels", img.shape[2])
print("Size of the Image Array", img.size)
print(cv2.countNonZero(img))
cv2.imshow("My Image", img)
cv2.waitKey()



