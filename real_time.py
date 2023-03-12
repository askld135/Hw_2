import cv2
from simple_facerec import SimpleFacerec

# Encode faces form a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

#Load Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    #Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        print(face_loc)
    
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()