import json
from tkinter import *
from camera import camara
from gui.config_screen import ventana_configuracion

def ventana():
    pantalla = Tk()
    pantalla.title("Reciclaje con visión artificial")
    pantalla.geometry("1408x768")
    imagenFondo = PhotoImage(file="assets/Fondo.png")
    fondo = Label(image=imagenFondo)
    fondo.place(x=0, y=0, relwidth=1, relheight=1)
    lblVideo = Label(pantalla)
    lblVideo.place(x=102, y=180)
    boton_configuracion = Button(pantalla, text='Configuracion', command=lambda: ventana_configuracion(pantalla))
    boton_configuracion.place(x=102, y=270)
    camara(lblVideo)
    pantalla.mainloop()

