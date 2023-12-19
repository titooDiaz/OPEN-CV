import cv2
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
imagen_path = os.path.join(script_dir, 'video1.mp4')
cap = cv2.VideoCapture(imagen_path)

bg = None

rojoBajo1 = np.array([0, 150, 40], np.uint8)
rojoAlto1 = np.array([8, 255, 255], np.uint8)
rojoBajo2 = np.array([170, 150, 40], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)

while True:
	ret, frame = cap.read()
	if ret == False: break

	if bg is None:
		bg = frame

	frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	maskRojo1 = cv2.inRange(frameHSV, rojoBajo1, rojoAlto1)
	maskRojo2 = cv2.inRange(frameHSV, rojoBajo2, rojoAlto2)
	mask = cv2.add(maskRojo1,maskRojo2)
	mask = cv2.medianBlur(mask, 13)
	kernel = np.ones((5,5),np.uint8)
	mask = cv2.dilate(mask, kernel, iterations=2)
	areaColor = cv2.bitwise_and(bg, bg, mask=mask)
	maskInv = cv2.bitwise_not(mask)
	sinAreaColor = cv2.bitwise_and(frame,frame,mask=maskInv)
	finalFrame = cv2.addWeighted(areaColor,1,sinAreaColor,1,0)
	cv2.imshow('Frame',frame)
	cv2.imshow('finalFrame',finalFrame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()