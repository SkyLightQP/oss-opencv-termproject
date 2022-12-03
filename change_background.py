import cv2


def change_background(image):
    changed_image = cv2.imread('./images/example_image.png')
    image = changed_image
    
    return image


# This image is for test. After implementing code of checking a background, change this variable to a background object.
image = cv2.imread('./images/input.png')
result = change_background(image)

cv2.imshow('Changed Image', image)
cv2.waitKey()
