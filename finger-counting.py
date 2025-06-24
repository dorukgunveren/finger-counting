import cv2 as cv
import mediapipe as mp

mpHand = mp.solutions.hands
hands = mpHand.Hands()

mpDraw = mp.solutions.drawing_utils

cap = cv.VideoCapture(0)

while True:
    succes, frame = cap.read()
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    if not succes:
        break
    
    results = hands.process(frame)
    
    lm_list = []
    extended_finger = []

    if results.multi_hand_landmarks:
        handLms = results.multi_hand_landmarks[0]
        mpDraw.draw_landmarks(frame, handLms, mpHand.HAND_CONNECTIONS)      
            
        for id,lm in enumerate(handLms.landmark):
            h, w, _ = frame.shape

            cy, cx = int(lm.y * h), int(lm.x * w)
            lm_list.append([id, cx, cy])

    if lm_list:
        if lm_list[0][2] > lm_list[9][2]:
            if lm_list[17][1] > lm_list[5][1]:
                if lm_list[4][1] > lm_list[3][1]:
                    extended_finger.append(0)
                else:
                    extended_finger.append(1)
                for id in [8, 12, 16, 20]:
                    if lm_list[id][2] < lm_list[id-2][2]:
                        extended_finger.append(1)
                    else:
                        extended_finger.append(0)
            else:
                if lm_list[4][1] > lm_list[3][1]:
                    extended_finger.append(1)
                else:
                    extended_finger.append(0)
                for id in [8, 12, 16, 20]:
                    if lm_list[id][2] < lm_list[id-2][2]:
                        extended_finger.append(1)
                    else:
                        extended_finger.append(0)
        else:
            if lm_list[17][1] > lm_list[5][1]:
                if lm_list[4][1] > lm_list[3][1]:
                    extended_finger.append(0)
                else:
                    extended_finger.append(1)
                for id in [8, 12, 16, 20]:
                    if lm_list[id][2] > lm_list[id-2][2]:
                        extended_finger.append(1)
                    else:
                        extended_finger.append(0)

            else:
                if lm_list[4][1] > lm_list[3][1]:
                    extended_finger.append(1)
                else:
                    extended_finger.append(0)
                for id in [8, 12, 16, 20]:
                    if lm_list[id][2] > lm_list[id-2][2]:
                        extended_finger.append(1)
                    else:
                        extended_finger.append(0)     

    if extended_finger:
        print(extended_finger, "\n")
        totalF = extended_finger.count(1)
        cv.putText(frame, "Total Fingers:"+ str(totalF), (30, 100), cv.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 8)

    cv.imshow("finger-counting", frame)

    quit = cv.waitKey(1)
    if quit != -1:
        break