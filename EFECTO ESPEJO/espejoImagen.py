import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
imagen_path = os.path.join(script_dir, 'ave.jpg')
imagen = cv2.imread(imagen_path)
flip_1 = cv2.flip(imagen,10)

cv2.imshow('flip_1',flip_1)
cv2.waitKey(0)