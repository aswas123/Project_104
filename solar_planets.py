import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(60,100),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=2.5,color=(0,0,200))
cv2.putText(img,"Mercury",(115,185),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(255,50,0))
cv2.putText(img,"Venus",(190,260),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(0,0,155))
cv2.putText(img,"Earth",(285,170),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(200,0,0))
cv2.putText(img,"Mars",(383,255),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Jupiter",(450,80),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=1,color=(255,255,255))
cv2.putText(img,"Saturn",(750,290),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Uranus",(960,140),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.6,color=(255,255,255))
cv2.putText(img,"Neptune",(1111,290),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.6,color=(255,255,255))
cv2.imshow("Output",img)
cv2.waitKey(0)