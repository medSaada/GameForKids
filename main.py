from cvzone.HandTrackingModule import HandDetector
import cv2
import requests
import random
import time

url = 'http://172.20.10.4/data'
ip_address = "http://172.20.10.5:81/stream"
cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8, maxHands=2)

random_int = random.randint(0, 5)
print(random_int)
while True:
    # Obtenir le cadre de l'image
    success, img = cap.read()

    # Retrouver la main et ses repères
    hands, img = detector.findHands(img)  # avec dessin
    # hands = detector.findHands(img, draw=False) # sans dessin

    if hands:
        # Main 1
        hand1 = hands[0]
        #hand2=hands[1]
        lmList1 = hand1["lmList"]  # Liste de 21 points de repère
        bbox1 = hand1["bbox"]  # Informations sur la boîte englobante x,y,w,h
        centerPoint1 = hand1['center']  # centre de la main cx,cy
        handType1 = hand1["type"]  # Handtype Left ou Right

        fingers1 = detector.fingersUp(hand1)
        #fingers2 = detector.fingersUp(hand2)
        #print(fingers1)

        if fingers1.count(1)==random_int:
            start_time = time.time()
            elapsed_time = time.time() - start_time# temps de départ

            # Code à chronométrer

            if elapsed_time>3:

                print("hand founded")
                response = requests.get(url)
                # if fingers1.count(1) == 2:
                #
                #     #response = requests.get("http://172.20.10.4/off")










    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
