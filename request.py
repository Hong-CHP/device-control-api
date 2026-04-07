import cv2
import requests

url = 'http://localhost:3000/event'

cap = cv2.VideoCapture(0)
# Location: https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml [following]
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if face_cascade is None: 
    print('Face cascade model loading failed.')
    exit()

last_state = None
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    if len(faces) > 0:
        state = '1'
    else:
        state = '0'
    
    if state != last_state:
        if state == '1':
            requests.post(url, json={
                "type": "face_detected",
            })
        else:
            requests.post(url, json={
                "type": "no_face",
            })
        last_state = state


    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()