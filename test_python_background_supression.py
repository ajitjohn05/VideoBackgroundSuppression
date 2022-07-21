import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

# importing the require package
#from py_avataaars import PyAvataaar  
  
# assigning various parameters to our avatar
#avatar = PyAvataaar()
  
# rendering the avatar in png format
#avatar.render_png_file("AVATAR_1.png")


cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('out.mp4')
#cap = cv2.VideoCapture('sample_cif.mp4')
#cap = cv2.VideoCapture('new_discussion.mp4')
#cap = cv2.VideoCapture('obama_video.mp4')
#cap = cv2.VideoCapture('mrf_conf_output.mp4')
cap.set(3, 640)
cap.set(4, 480)
# cap.set(cv2.CAP_PROP_FPS, 60)

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

imgBG = cv2.imread("background_image.JPG")
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
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)
    #imgOut = segmentor.removeBG(img,imgBG, threshold=0.8)

    imgStack = cvzone.stackImages([img, imgOut], 2,1)
    _, imgStack = fpsReader.update(imgStack)
    print(indexImg)
    cv2.imshow("image", imgStack)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg>0:
            indexImg -=1
    elif key == ord('d'):
        if indexImg<len(imgList)-1:
            indexImg +=1
    elif key == ord('q'):
        break