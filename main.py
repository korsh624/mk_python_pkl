import cv2
cap=cv2.VideoCapture(0)
while (True):
    # ret,frame=cap.read()
    frame=cv2.imread("./apelsin.jpg")
    frame=cv2.resize(frame,(800,600), interpolation=cv2.INTER_AREA)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
