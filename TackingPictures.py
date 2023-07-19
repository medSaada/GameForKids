import os.path

import cv2 as cv
import requests
import time


"""
Initialisation of the image from path

"""
pathRequest="http://172.20.10.5:81/stream"
"object of the image"
cap=cv.VideoCapture(0)

"""""""""""""""""""""
creating the path to store the data
"""""
path=r"D:\document\mes dos\doc\bureau\coding\dataCollecting\empty"
if not os.path.exists(path):
    os.makedirs(path)
    "we created the d"
##########################  The delays

startTime=time.time()
stepForTakingImage=2
nbrImage=0




while True:
    res,img=cap.read()
    grayScale=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    crop=cv.resize(grayScale,(96,96))
    cv.imshow("OUTPUT",crop)
    imageCounter=time.time()-startTime

    if imageCounter>stepForTakingImage:
        whereYouWrite=os.path.join(path,f"image_{int(nbrImage)}.bmp")

        cv.imwrite(whereYouWrite,crop)
        print("imageCapturedAndsAVED")
        startTime=time.time()
        nbrImage+=1
        print(nbrImage)


    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()