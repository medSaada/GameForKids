from cvzone.HandTrackingModule import HandDetector
from time import sleep
import cv2 as cv
cv.





#creating an object of detector
handDetector=HandDetector(detectionCon=0.8,maxHands=1)
# *******Example***********

while True:

    for _ in handDetector:

