import cv2
from csv import writer
import Hand_Tracking_Module as htm
from itertools import chain

detector = htm.handDetector(detectionCon=0.75)
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 16
count = 0
while True:
    count+=1
    ret, frame = cam.read()
    img = detector.findHands(frame)
    if not ret:
        print("failed to grab frame")
        break

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        realdata = []
        detectlist = detector.findPosition(img, draw=True)
        detection = list(chain.from_iterable(detectlist))
        # print(detection)
        for i in range(len(detection)):
            if i % 3 == 0 :
                continue
            else :
                realdata.append(detection[i])

        if realdata :
            xorigin = realdata[0]
            yorigin = realdata[1]
            for i in range(len(realdata)):
                if i % 2 == 0 :
                    realdata[i] = realdata[i] - xorigin
                else:
                    realdata[i] = realdata[i] - yorigin
            realdata.append(img_counter)
            # img_counter += 1
            if len(realdata) == 43 :
                print(realdata)
                with open('data.csv', 'a') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow(realdata)
                    f_object.close()
            else :
                continue
    cv2.imshow("test", img)
cam.release()

cv2.destroyAllWindows()

# features and label of the dataset
# 0X,0Y,1X,1Y,2X,2Y,3X,3Y,4X,4Y,5X,5Y,6X,6Y,7X,7Y,8X,8Y,9X,9Y,10X,10Y,11X,11Y,12X,12Y,13X,13Y,14X,14Y,15X,15Y,16X,16Y,17X,17Y,18X,18Y,19X,19Y,20X,20Y,OUTPUT


