import cv2
from facial_recognition import face
from watermark import watermark

img = cv2.imread("./images/face.png")

result_face = face(img)
# TODO: Detect background
# TODO: Change background
result_watermark = watermark(result_face)

result_watermark.show()
