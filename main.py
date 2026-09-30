import cv2
import face_recognition
import pandas as pd
from datetime import datetime

video_capture = cv2.VideoCapture(0)
attendance_list = []

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)

    for (top, right, bottom, left) in face_locations:
        name = "User"
        now = datetime.now()
        attendance_list.append([name, now.strftime("%Y-%m-%d %H:%M:%S")])

        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

df = pd.DataFrame(attendance_list, columns=["Name", "Time"])
df.to_csv("attendance.csv", index=False)

video_capture.release()
cv2.destroyAllWindows()
