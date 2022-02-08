import cv2
# cap=cv2.VideoCapture(0)
while (True):
    # ret,frame=cap.read()
    frame=cv2.imread("./input.jpg")
    frame=cv2.resize(frame,(800,600), interpolation=cv2.INTER_AREA)
    cv2.imshow("Frame", frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, (179,204,189),(212,243,243))
    thresh = cv2.GaussianBlur(thresh, (5, 5), 2)
    conts, heir = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if conts:
        cv2.drawContours(frame, conts, -1, (255, 0, 0), 5)
        # print(conts)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break

        #(179.204.189),(212.243.243)
