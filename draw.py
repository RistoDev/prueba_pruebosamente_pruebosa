import cv2

def dibujar(frame, p1, p2, cls, conf):
    x1, y1 = p1
    x2, y2 = p2
    nombre = f"{cls} {conf*100:.1f}%"
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.rectangle(frame, (x1, y1 - 25), (x1 + 180, y1), (0, 255, 0), -1)
    cv2.putText(frame, nombre, (x1 + 5, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)