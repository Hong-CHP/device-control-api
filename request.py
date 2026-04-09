import cv2
import time
import requests

THERESHOLD = 5
MIN_INTERVAL = 0.5

url = 'http://localhost:3000/event'

cap = cv2.VideoCapture(0)

# Location: https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml [following]
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if face_cascade is None: 
    print('Face cascade model loading failed.')
    exit()

face_detected_frames = 0
face_lost_frames = 0
state = 0
last_state = 0

# register last_time as starter
last_time = 0

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

    # deboudance by face detected on continue frames
    if len(faces) > 0:
        face_detected_frames += 1
        face_lost_frames = 0
    else:
        face_lost_frames += 1
        face_detected_frames = 0

    # deboudance once again by time
    if face_detected_frames >= THERESHOLD:
        if time.time() - last_time >= MIN_INTERVAL:
            state = 1
            last_time = time.time()

    if face_lost_frames >= THERESHOLD:
        if time.time() - last_time >= MIN_INTERVAL:
            state = 0
            last_time = time.time()
    
    if state != last_state:
        if state == 1:
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