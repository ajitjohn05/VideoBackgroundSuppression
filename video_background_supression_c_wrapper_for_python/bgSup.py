import cffi
import sys
import traceback
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
from PIL import Image
import numpy as np


ffi = cffi.FFI()
ffi.cdef(open('interface.h').read())


# Convert input buffer to repr(buffer).
@ffi.callback("void (char*, int, int, int)")
def startStream(buffer, buffer_len, width, height):

	#convert c buffer to bytes
	data = ffi.buffer(buffer, buffer_len)[:]
	#decoded = np.frombuffer(data, dtype=np.uint8)
	decoded = np.fromstring(data, dtype=np.uint8)
	decoded = decoded.reshape(width*3//2,height)
	bgr = cv2.cvtColor(decoded, cv2.COLOR_YUV2BGR_I420)
	
	segmentor = SelfiSegmentation()
	imgOut = segmentor.removeBG(bgr, (255,0,255), threshold=0.83)

	imgStack = cvzone.stackImages([bgr, imgOut], 2,1)
	cv2.imshow("BG", imgStack)
	key = cv2.waitKey(10)
"""
#ORIGINAL CODE 
	cap = cv2.VideoCapture('2.mp4')
	cap.set(3, 640)
	cap.set(4, 480)
	# cap.set(cv2.CAP_PROP_FPS, 60)
	print("str->",str(buffer))
	segmentor = SelfiSegmentation()
	fpsReader = cvzone.FPS()

	imgBG = cv2.imread("test2.jpg")
	imgBG=cv2.resize(imgBG,(640,480),interpolation = cv2.INTER_AREA)

	listImg = os.listdir("BackgroundImages")
	imgList = []
	for imgPath in listImg:
	    img = cv2.imread(f'BackgroundImages/{imgPath}')
	    img = cv2.resize(img,(640,480),interpolation = cv2.INTER_AREA)
	    imgList.append(img)

	indexImg = 0

	while True:
	    success, img = cap.read()
	    img = cv2.resize(img, (640, 480))
	    # imgOut = segmentor.removeBG(img, (255,0,255), threshold=0.83)
	    #imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)
	    imgOut = segmentor.removeBG(img,imgBG, threshold=0.8)

	    imgStack = cvzone.stackImages([img, imgOut], 2,1)
	    _, imgStack = fpsReader.update(imgStack)
	    #print(indexImg)
	    cv2.imshow("image", imgStack)
	    #cv2.imshow("modifiedimage", imgOut)
	    key = cv2.waitKey(1)
	    if key == ord('q'):
	    	break
"""

def fill_api(ptr):
    global api
    api = ffi.cast("struct API*", ptr)
    #add functions here
    api.startStream = startStream

