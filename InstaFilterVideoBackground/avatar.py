
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
from PIL import Image
import numpy as np
import sys

#n=len(sys.argv)
#print("Total arg",n)

def put_dog_filter(dog, fc, x, y, w, h):
    face_width = w
    face_height = h

    dog = cv2.resize(dog, (int(face_width * 1.5), int(face_height * 1.95)))
    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if dog[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = dog[i][j][k]
    return fc

def put_hat(hat, fc, x, y, w, h):
    face_width = w
    face_height = h

    hat_width = face_width + 1
    hat_height = int(0.50 * face_height) + 1

    hat = cv2.resize(hat, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if hat[i][j][k] < 235:
                    fc[y + i - int(0.40 * face_height)][x + j][k] = hat[i][j][k]
    return fc


def put_glass(glass, fc, x, y, w, h):
    face_width = w
    face_height = h

    hat_width = face_width + 1
    hat_height = int(0.50 * face_height) + 1

    glass = cv2.resize(glass, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if glass[i][j][k] < 235:
                    fc[y + i - int(-0.20 * face_height)][x + j][k] = glass[i][j][k]
    return fc


width = int(sys.argv[1])
height = int(sys.argv[2])
choice = int(sys.argv[3])
#print("choice",choice)

imgBG = cv2.imread("2.JPG")
imgBG=cv2.resize(imgBG,(height,width),interpolation = cv2.INTER_AREA)
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
hat=cv2.imread('hat.png')
glass=cv2.imread('glasses.png')
dog=cv2.imread('dog.png')

width_1 = int(width)*1.5
shape = (int(width_1),int(height))
#print("Entry");
fpIn  = open("in.yuv", 'rb')
fpOut = open("out.yuv", 'wb')
frame_len = (width * (height * 3 // 2))

#new code to read from file
ffv = open("SpX54_352_288.yuv", 'rb')


while 1:
        file1 = open("param.txt");
        line = file1.readline()
        if not line:
            print("Empty")
            break
        file1.close()
        imgBG = cv2.imread(line.strip())
        imgBG = cv2.resize(imgBG,(height,width),interpolation = cv2.INTER_AREA)
        raw =  fpIn.read(int(frame_len))
        yuv = np.frombuffer(raw, dtype=np.uint8)
        yuv = yuv.reshape(shape)
        bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)

        #read video for background
        bgVid =  ffv.read(int(frame_len))
        bgVidyuv = np.frombuffer(bgVid, dtype=np.uint8)
        bgVidyuv = bgVidyuv.reshape(shape)
        bgVidbgr = cv2.cvtColor(bgVidyuv, cv2.COLOR_YUV2BGR_I420)
        #read video ends
        
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        fl = face.detectMultiScale(gray,1.19,7)

        if choice == 1:
                segmentor = SelfiSegmentation()
                imgOut = segmentor.removeBG(bgr, bgVidbgr, threshold=0.83)
                cv2.imshow("frame", imgOut)
                ret = cv2.cvtColor(imgOut, cv2.COLOR_BGR2YUV_I420)
                cv2.waitKey(10)

        elif choice == 2:
                #blur
                # Step 2: Convert to the HSV color space
                hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
                # Step 3: Create a mask based on medium to high Saturation and Value
                # - These values can be changed (the lower ones) to fit your environment
                mask = cv2.inRange(hsv, (0, 75, 40), (180, 255, 255))
                # We need a to copy the mask 3 times to fit the frames
                mask_3d = np.repeat(mask[:, :, np.newaxis], 3, axis=2)
                # Step 4: Create a blurred frame using Gaussian blur
                blurred_frame = cv2.GaussianBlur(bgr, (25, 25), 0)
                # Step 5: Combine the original with the blurred frame based on mask
                outframe = np.where(mask_3d == (255, 255, 255), bgr, blurred_frame)
                ret = cv2.cvtColor(outframe, cv2.COLOR_BGR2YUV_I420)

        elif choice == 3:
            fpInAv  = open("AVATAR_352x288.yuv", 'rb')
            #frame_len = (width * (height * 3 // 2))
            i=1
            while i<10:
                raw =  fpInAv.read(int(frame_len))
                yuv = np.frombuffer(raw, dtype=np.uint8)
                yuv = yuv.reshape(shape)
                print(shape)
                bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)
                cv2.imshow("Blur Effect", bgr)
                cv2.waitKey(30)
                ret = cv2.cvtColor(bgr, cv2.COLOR_BGR2YUV_I420)
                fpOut.write(ret)
                i=i+1
                #print(i)
            fpInAv.close()
            fpIn.close()
            fpOut.close()

        elif choice == 4:
                for (x, y, w, h) in fl:
                        bgr = put_hat(hat, bgr, x, y, w, h)
                        bgr = put_glass(glass, bgr, x, y, w, h)
                        ret = cv2.cvtColor(bgr, cv2.COLOR_BGR2YUV_I420)
        else:
                for (x, y, w, h) in fl:
                        bgr = put_dog_filter(dog, bgr, x, y, w, h)
                        ret = cv2.cvtColor(bgr, cv2.COLOR_BGR2YUV_I420)

        #ret = cv2.cvtColor(imgOut, cv2.COLOR_BGR2YUV_I420)
        fpOut.write(ret)
#cv2.waitKey(1500)

fpIn.close()
fpOut.close()
