# 1.- Importamos la libreria
import cv2

# 2.- Cargamos la imagen
image = cv2.imread("archivos\mark.png")

# 3.- Aplicamos filtros en escala 
# de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold( gray, 255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY, 9, 9)

# 4.- Aplicamos otro filtro bilateral 
# para suavisar la imagen y combinamos las
# imagenes para crear el efecto cartoon
color = cv2.bilateralFilter(image, 9, 250, 250)
cartoon = cv2.bitwise_and(color, image, 
                          mask=edges)

# 5.- Mostramos el resultado
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)