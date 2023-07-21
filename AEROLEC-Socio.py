from cvzone.HandTrackingModule import HandDetector
import cv2
import requests
import random
import time


#random value:
random_value = random.randint(0, 5)
random_yd=random.randint(0,1)
#print(random_value)

#partie selection d'image:


#declaration objet detector
detector = HandDetector(detectionCon=0.8, maxHands=2)


def saada1_display(img,i):
    if i==0:
        cv2.putText(img,"Numero zero",(4,78),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    elif i==1:
        cv2.putText(img, "Numero un",(4,78), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    elif i==2:
        cv2.putText(img, "Numero DEUX",(4,78), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    elif i==3:
        cv2.putText(img, "Numero TROIS",(4,78), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    elif i==4:
        cv2.putText(img, "Numero QUATRE",(4,78), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    elif i==5:
        cv2.putText(img, "Numero CINQ", (4,78),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)

def yd_random(img,random_yd):
    if random_yd==0:

        cv2.putText(img, "MAIN DROITE", (4, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
        return "Right"
    if random_yd==1:

        cv2.putText(img, "MAIN GAUCHE", (4, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
        return "Left"


counter=0
url = 'http://172.20.10.4/forward'
ip_address1 = "http://172.20.10.5/ledon"
ip_address2 = "http://172.20.10.5/ledoff"

#une fonction clinotant

def saada_happy(i):
    if i==0:
        response=requests.get(ip_address1)
        time.sleep(2)
        response = requests.get(ip_address2)
    else:
        response=requests.get(ip_address1)












cap = cv2.VideoCapture(0)
while True:
    # Obtenir le cadre de l'image
    success, img = cap.read()
    #partie prendre random nombre le display it
    saada1_display(img, random_value)
    hand_type=yd_random(img,random_yd)

    #print(hand_type)
    #partie detection
    # Retrouver la main et ses repères
    hands, img = detector.findHands(img)  # avec dessin

    #hands est une liste
    if len(hands):
        hand1 = hands[0]
        type_dlyd=hands[0]['type']
        #print(type_dlyd)
        if type_dlyd==hand_type:



            fingers1 = detector.fingersUp(hand1)
            if fingers1.count(1) == random_value:
                counter += 1
                cv2.putText(img, str(counter), (4, 180), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
                if (counter == 100):
                    requests.get("http://172.20.10.5/ledon")
                    counter=0


    cv2.imshow("SOCIO CARAVANE AEROLEC ACTIVITE", img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        requests.get("http://172.20.10.5/ledoff")
        break

cap.release()
cv2.destroyAllWindows()
"""""git reposetory storage stage staging area"""

"onother modification"
