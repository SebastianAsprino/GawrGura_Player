from tkinter import *
import tkinter as tk
ventana = Tk()
ventana.title("Music Player")
ventana.geometry("800x600")
ventana.iconbitmap(".image\gura.ico")
ventana.config(bg="black")
ventana.resizable(0,0)
boton = tk.Button (text= ":D")
boton.place(x=50, y=50 )
ventana.mainloop()
