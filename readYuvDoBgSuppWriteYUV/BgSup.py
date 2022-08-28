import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
from PIL import Image
import numpy as np
import sys

#n=len(sys.argv)
#print("Total arg",n)


width = int(sys.argv[1])
height = int(sys.argv[2])
#print("width",width);
#print("height",height);
width_1 = int(width)*1.5
shape = (int(width_1),int(height))
#print("Entry");
fpIn  = open("in.yuv", 'rb')
fpOut = open("out.yuv", 'wb')
frame_len = (width * (height * 3 // 2))

raw =  fpIn.read(int(frame_len))
yuv = np.frombuffer(raw, dtype=np.uint8)
yuv = yuv.reshape(shape)
bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)
segmentor = SelfiSegmentation()
imgOut = segmentor.removeBG(bgr, (255,0,255), threshold=0.83)
#cv2.imshow("frame", imgOut)
ret = cv2.cvtColor(imgOut, cv2.COLOR_BGR2YUV_I420)
fpOut.write(ret) 
#cv2.waitKey(1500)

fpIn.close()
fpOut.close();
