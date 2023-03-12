import cv2
from simple_facerec import SimpleFacerec

# Encode faces form a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

#Load Camera
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1440)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    ret, frame = cap.read()
    
    #Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        top, right, bottom, left = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        #y1, x1, y2, x2
        cv2.putText(frame, name,(right,top - 10),cv2.FONT_HERSHEY_DUPLEX, 1, (138,43,226), 2)
        cv2.rectangle(frame, (right, top), (left, bottom),(230, 230, 250), 4)
    
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()