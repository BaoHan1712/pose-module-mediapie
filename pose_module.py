import cv2 
import mediapipe as mp
import time
# nhận diện pose
mpPose = mp.solutions.pose
pose = mpPose.Pose()
# vẽ các khớp nối ra
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
pTime = 0

while True:
    success,img=cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # ghi các điểm kết quả ra
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h , w, c = img.shape
            cx, cy = int(w * lm.x), int(h * lm.y)
#ghi thời gian thực
    cTime=time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),3)
    cv2.imshow("RealTime", img)
# Thoát khỏi vòng lặp 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
