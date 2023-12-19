import cv2
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

modelo = os.path.join(script_dir, 'modelo.xml')
faceClassif = cv2.CascadeClassifier(modelo)

imagen_path = os.path.join(script_dir, 'oficina.png')
imagen = cv2.imread(imagen_path)
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30,30),
	maxSize=(200,200))

for (x,y,w,h) in faces:
	cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()