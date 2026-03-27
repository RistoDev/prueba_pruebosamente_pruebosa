import cv2
from settings.settings import CAMERA_INDEX
import imutils
from tkinter import Label
from PIL import Image, ImageTk
from detector import analizar_frame


def camara(lblVideo: Label):
    global cap, labelVideo
    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    labelVideo = lblVideo

    if cap is None:
        print("Cámara no disponible")
    actualizar()

def actualizar():
    ret, frame = cap.read()

    if ret == False:
        return cap.release()

    frame = imutils.resize(frame, width=668, height=485)
    frame_show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    analizar_frame(frame, frame_show)
    im = Image.fromarray(frame_show)
    img = ImageTk.PhotoImage(im)
    labelVideo.configure(image=img)
    labelVideo.image = img
    labelVideo.after(50, actualizar)