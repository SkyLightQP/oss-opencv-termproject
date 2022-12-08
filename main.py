import cv2

from facial_recognition import face
from watermark import watermark
from change_background import change_background


img = cv2.imread("./images/ex2.png")
background = cv2.imread("./images/example_image.jpg")

result_face = face(img)
# TODO: Detect background
# result_changed = change_background(result_face, mask, background)
result_watermark = watermark(result_face)

result_watermark.show()
