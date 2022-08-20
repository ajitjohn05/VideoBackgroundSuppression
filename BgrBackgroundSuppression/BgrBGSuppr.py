"""Purpose of this script is to 
-> read BGR buff
-> Remove background and Add new background
-> return processed BGR
"""
import cv2
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation

def VideoCaptureBGR(fileName):
	fp = open("out2.bgr", "rb")
	return fp;

def ReadBgrFrame(fp, width, height):
	frameSize = width*height*3 
	bgr = fp.read(frameSize);
	img =  np.frombuffer(bgr, dtype = np.uint8)
	img = img.reshape(height, width,3)
	imgOut = segmentor.removeBG(img,imgBG, threshold=0.8)
	#imgOut = segmentor.removeBG(img, (255,0,255), threshold=0.83)
	return imgOut

segmentor = SelfiSegmentation()	
fp = VideoCaptureBGR("out2.bgr")

imgBG = cv2.imread("test2.jpg")
imgBG = cv2.resize(imgBG,(352,288),interpolation = cv2.INTER_AREA)
	
while 1:
	imgOut = ReadBgrFrame(fp, 352, 288)
	
	cv2.imshow("frame", imgOut)
	cv2.waitKey(30)
