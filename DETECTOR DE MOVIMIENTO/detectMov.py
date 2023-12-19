import cv2
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
imagen_path = os.path.join(script_dir, 'video.mp4')
video = cv2.VideoCapture(imagen_path)

i = 0
while True:
	ret, frame = video.read()
	if ret == False: break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	if i == 20:
		bgGray = gray
	if i > 20:
		dif = cv2.absdiff(gray, bgGray)
		_, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
		cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		
		for c in cnts:
			area = cv2.contourArea(c)
			if area > 9000:
				x,y,w,h = cv2.boundingRect(c)
				cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)

	cv2.imshow('Frame',frame)

	i = i+1
	if cv2.waitKey(30) & 0xFF == ord ('q'):
		break
video.release()
