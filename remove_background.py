import cv2
import numpy as np

def remove_background():
  
  # load image with alpha channel
  img = cv2.imread('ex2.png', cv2.IMREAD_UNCHANGED)

  # make white image
  white = img[:,:,3]

  # make normal image
  bgr = img[:,:,0:3]

  # select white part of picture
  lower_value = (240,245,240)
  upper_value = (255,255,255)
  mask = cv2.inRange(bgr, lower_value, upper_value)

  # change background into green where the mask is white
  greenbg = bgr.copy()
  greenbg[mask==255] = (0,180,0)

  return greenbg

  cv2.imshow('bgr_new',greenbg)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


