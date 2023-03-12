#"https://github.com/ageitgey/face_recognition/blob/master/README_Korean.md"

import cv2
import face_recognition

img = cv2.imread("Michael_Douglas.jpg")

cv2.imshow("Img", img)
cv2.waitKey(0)