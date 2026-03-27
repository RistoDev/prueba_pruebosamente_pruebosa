from ultralytics import YOLO
from settings.settings import CLASSES_NAME, CONFIDENCE_THRESHOLD, DATASET_DIR_CUT, DATASET_DIR_FULL, SECONDS_TO_SAVE_CUT, SECONDS_TO_SAVE_FULL
from draw import dibujar
import time
import cv2

modelo = YOLO('Modelos/best.pt')
cut_timestamp = None
full_timestamp = None

def analizar_frame(frame, frame_show):
    global cut_timestamp, full_timestamp
    results = modelo(frame, stream=True, verbose=False)
    saved = False

    for result in results:
        timestamp = int(time.time())
        boxes = result.boxes

        #print(boxes)
        if len(boxes) == 0:
            if full_timestamp == None or full_timestamp + SECONDS_TO_SAVE_FULL < timestamp:
                full_timestamp = timestamp
                #cv2.imwrite(DATASET_DIR_FULL + '/' + str(timestamp) + '.jpg', frame)
                #print(f'{timestamp} imagen sin objeto reconocido guardado')
            continue

        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            if x1 < 0: x1 = 0
            if y1 < 0: y1 = 0
            if x2 < 0: x2 = 0
            if y2 < 0: y2 = 0

            cls = int(box.cls[0])
            cls_name = CLASSES_NAME[cls]
            conf = float(box.conf[0])
            dibujar(frame_show, (x1, y1), (x2, y2), cls_name, conf)

            #print(f'{CLASSES_NAME[cls]}: {conf * 100}%')

            if conf < CONFIDENCE_THRESHOLD:
                if cut_timestamp == None or cut_timestamp + SECONDS_TO_SAVE_CUT < timestamp:
                    saved = True
                    print(f'{timestamp} patata')
                    cv2.imwrite(DATASET_DIR_CUT + '/' + f'{i}-{cls_name}-{int(conf * 100)}%' + str(timestamp) + '.jpg', frame[y1:y2, x1:x2])

    if saved == True: cut_timestamp = timestamp