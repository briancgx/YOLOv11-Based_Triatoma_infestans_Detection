from ultralytics import YOLO
import cv2

model = YOLO("final-model.pt")

cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo capturar el fotograma.")
        break

    resultados = model.predict(frame, imgsz=640, verbose=False, conf=0.80) 

    if len(resultados[0].boxes) > 0:  
        anotaciones = resultados[0].plot()  
    else:
        anotaciones = frame  

    cv2.imshow("Detección con YOLO11 (Confianza > 90%)", anotaciones)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
