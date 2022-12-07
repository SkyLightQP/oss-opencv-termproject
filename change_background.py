import cv2


def change_background(origin, mask, background):
    origin_height = origin.shape[0]
    origin_width = origin.shape[1]
    resized_background = cv2.resize(background, dsize=(origin_width, origin_height))
    
    # copyTo() only running in same size.
    result = cv2.copyTo(origin, mask, resized_background)
    
    return result



background = cv2.imread('./images/input.png')

# The Function required original image and mask.
result = change_background(result_img, mask, background)

cv2.imshow('Changed Image', result)
cv2.waitKey()
