import cv2
import numpy

img = cv2.imread('ex2.jpg')

# Define lower and uppper color limits which contain background
# Expect people with black clothes
low = numpy.array([232, 238, 232])
high = numpy.array([255, 255, 255])

white_bg = cv2.inRange(img, low, high)


# Clean wrong parts
parts = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
cleaned_img = cv2.morphologyEx(white_bg, cv2.MORPH_CLOSE, parts)

# invert black & white image
mask = 255 - cleaned_img

# apply to image
result_img = cv2.bitwise_and(img, img, mask=mask)


cv2.imshow('original', img)
cv2.imshow('cleaned', cleaned_img)
cv2.imshow('result', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
