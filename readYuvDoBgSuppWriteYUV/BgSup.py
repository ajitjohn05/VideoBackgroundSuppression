import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
from PIL import Image
import numpy as np

width = 288
height = 352
shape = (int(width*1.5),int(height))
print("Entry");
fpIn  = open("in.yuv", 'rb')
fpOut = open("out.yuv", 'wb')
frame_len = (width * (height * 3 // 2))

while 1:
	raw =  fpIn.read(int(frame_len))
	yuv = np.frombuffer(raw, dtype=np.uint8)
	yuv = yuv.reshape(shape)
	bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)
	segmentor = SelfiSegmentation()
	imgOut = segmentor.removeBG(bgr, (255,0,255), threshold=0.83)
	cv2.imshow("frame", imgOut)
	ret = cv2.cvtColor(imgOut, cv2.COLOR_BGR2YUV_I420)
	fpOut.write(ret) 
	cv2.waitKey(30)
print("Close")
fpIn.close()
fpOut.close();
