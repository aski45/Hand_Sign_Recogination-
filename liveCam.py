# importing libreries
import cv2                                    # Opencv
import Hand_Tracking_Module as htm            # Mediapipe module from Google
from itertools import chain

#importing machine learning model
import learning

# initialize camera
cap = cv2.VideoCapture(0)

# inititalizing detector from hand_tracking_module
detector = htm.handDetector(detectionCon=0.75)


 # empty final output variable
answer = 0
output = 0

# capturing frames from camera until closing camera
while(cap.isOpened()):
    testlist = []           # empty list for gathering 42 cordinates ( 20 for each x and y of a point)

    # reading and storing frames in img
    success , img = cap.read()

    # sending img for detecting cordinates
    img = detector.findHands(img)

    # gathering cordinates returned by Hand_Tracking_Module
    lmlist = detector.findPosition(img , draw=False)

    # converting multi dimensional array  to 1d list
    cords = list(chain.from_iterable(lmlist))
    # now list contains 63 coloums, with 21 coloms indexes at every third position
    # hence filteing the list to only 42 items
    if cords:
        for i in range(len(cords)):
            if i % 3 == 0:
                continue
            else:
                testlist.append(cords[i])
        # now we have a very wide range of cordinates in the list
        # so normlizing all cordinates with the 0 th cordinate

        # origin shifting
        if testlist:
            xorigin = testlist[0]
            yorigin = testlist[1]
            for i in range(len(testlist)):
                if i % 2 == 0:
                    testlist[i] = testlist[i] - xorigin
                else:
                    testlist[i] = testlist[i] - yorigin

        # print(len(testlist))

        # sending captured cordinates to trined model
        answer = learning.getanswer(testlist)

        # storing prdiction list to anser variable
        output = answer[0]
    # we have got integer from model converting and rendering as cahrecter

    # for char
    cv2.putText(img , chr(output + 65), (45 , 375) , cv2.FONT_HERSHEY_PLAIN , 5 ,( 25 ,217, 202    ), 10 ) # B G R

    # for digit
    #cv2.putText(img, str(answer), (45, 375), cv2.FONT_HERSHEY_PLAIN, 5, (25, 217, 202), 10)  # B G R
    # live video capture
    cv2.imshow("LIVE RECOGNATION (Press 'Q' to Quit)",img)

    # condition for stoping live cam
    if cv2.waitKey(1) == 113 :    # if pressed "Q" button on the keyboard
        break
