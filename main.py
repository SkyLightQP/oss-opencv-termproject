import cv2

from facial_recognition import face
from watermark import watermark
from change_background import change_background
from remove_background import remove_background


img = cv2.imread("./images/ex2.png")
result_face = face(img)

result_background, mask = remove_background(img)

background = cv2.imread("./images/face.png")
result_changed = change_background(result_face, mask, background)

result_watermark = watermark(result_changed)

result_watermark.show()
