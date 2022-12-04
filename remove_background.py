import cv2
import numpy

def remove_background():
  
  img = cv2.imread('ex1.jpg')
  hh, ww = img.shape[:2]

  # Define lower and uppper color limits which contain background
  # Expect people with black clothes
  low = numpy.array([255, 220, 220])
  high = numpy.array([255, 255, 255])

  # Create mask to only select black
  img = cv2.inRange(img, low, high)

  # Repeat untill background color is unified
  low = numpy.array([80, 80, 80])
  high = numpy.array([255, 155, 155])

  # Create mask to only select black
  img = cv2.inRange(img, low, high)

  # Repeat untill background color is unified
  low = numpy.array([80, 80, 80])
  high = numpy.array([130, 255, 255])

  # Create mask to only select black
  img = cv2.inRange(img, low, high)

  # Repeat untill background color is unified
  low = numpy.array([80, 80, 80])
  high = numpy.array([130, 255, 255])

  # Create mask to only select black
  white_bg = cv2.inRange(img, low, high)




  # Clean wrong parts
  parts = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
  cleaned_img = cv2.morphologyEx(white_background, cv2.MORPH_CLOSE, parts)

  # invert black & white image
  inverted_img = 255 - cleaned_img

  # apply to image
  result_img = cv2.bitwise_and(img, img, inverted_img=inverted_img)


  cv2.imshow('white', white_bg)
  cv2.imshow('cleaned', cleaned_img)
  cv2.imshow('inverted', inverted_img)
  cv2.imshow('result', result_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
