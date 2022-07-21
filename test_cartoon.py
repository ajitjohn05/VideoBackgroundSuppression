import cv2
import cvzone
import numpy as np
import matplotlib.pyplot as plt
cap = cv2.VideoCapture('obama_video.mp4')
cap.set(3, 640)
cap.set(4, 480)
#img = cv2.imread("obama_test.JPG")
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (640, 480))
    #img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
    #plt.figure(figsize=(10,10))
    #plt.imshow(img)
    #plt.axis("off")
    #plt.title("Original Image")
    #plt.show()
    cv2.imshow("original image", img)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    #plt.figure(figsize=(10,10))
    #plt.imshow(gray,cmap="gray")
    #plt.axis("off")
    #plt.title("Grayscale Image")
    #plt.show()
    #cv2.imshow("Grayscale image", gray)
    
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    #plt.figure(figsize=(10,10))
    #plt.imshow(edges,cmap="gray")
    #plt.axis("off")
    #plt.title("Edged Image")
    #plt.show()
    #cv2.imshow("Edged image", edges)
    
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    #plt.figure(figsize=(10,10))
    #plt.imshow(cartoon,cmap="gray")
    #plt.axis("off")
    #plt.title("Cartoon Image")
    #plt.show()
    #cv2.imshow("Cartoon image", cartoon)
    imgStack = cvzone.stackImages([img, gray],2,1)
    cv2.imshow("image", imgStack)

