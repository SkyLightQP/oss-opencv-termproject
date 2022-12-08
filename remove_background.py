import cv2
import numpy as np

def remove_background(img):
  # make normal image
  bgr = img[:,:,0:3]

  # select white part of picture
  lower_value = (240,245,240)
  upper_value = (255,255,255)
  mask = cv2.inRange(bgr, lower_value, upper_value)

  # change background into green where the mask is white
  greenbg = bgr.copy()
  greenbg[mask==255] = (0,180,0)

  return (greenbg, mask)

