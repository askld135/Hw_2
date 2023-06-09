#"https://github.com/ageitgey/face_recognition/blob/master/README_Korean.md"
#"https://ukayzm.github.io/unknown-face-classifier/"

import cv2
import face_recognition
from simple_facerec import SinpleFacerec

img = cv2.imread("Michael_Douglas.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread("images/Keum-Kang-seon.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding],img_encoding2)
print(result)

cv2.imshow("Img", img)
cv2.imshow("Img2", img2)
cv2.waitKey(0)