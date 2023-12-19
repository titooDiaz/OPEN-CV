import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
imagen_path = os.path.join(script_dir, 'cartas.jpg')
imagen = cv2.imread(imagen_path)

grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(grises, 100, 200)

cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Imagen', grises)
cv2.waitKey(0)
cv2.destroyAllWindows()

ctns, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
ctns = sorted(ctns, key=cv2.contourArea, reverse=True)

area_minima = 500 
ctns_filtrados = [contorno for contorno in ctns if cv2.contourArea(contorno) > area_minima]
contador_cartas = 0
for contorno in ctns_filtrados:
    perimetro = cv2.arcLength(contorno, True)
    #                         contorno,   aproximacion  , cerrado o abierto
    approx = cv2.approxPolyDP(contorno, 0.02 * perimetro, True)
    if len(approx) == 4:
        contador_cartas += 1

cv2.drawContours(imagen, [contorno for contorno in ctns_filtrados if len(cv2.approxPolyDP(contorno, 0.02 * cv2.arcLength(contorno, True), True)) == 4], -1, (0, 0, 255), 2)
texto = 'Cartas encontradas: ' + str(contador_cartas)
#FORMATO DE COLOR BGR
cv2.putText(imagen, texto, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 1)

cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagen_path = os.path.join(script_dir, 'cartas_resultado.jpg')
cv2.imwrite(imagen_path, imagen)
