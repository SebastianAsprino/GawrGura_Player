from tkinter import *
from tkinter import filedialog, Listbox
from PIL import ImageTk, Image
import tkinter as tk
from pathlib import Path
from tinytag import TinyTag
import io
import pygame

window = Tk()
window.geometry("500x500")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

pygame.mixer.init()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

canvas = tk.Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

AudioMetadata = TinyTag.get('Music/14-I-Will-Sing.mp3', image=True)

im = AudioMetadata.get_image()

pi = Image.open(io.BytesIO(im))

def add_song():
    song = filedialog.askopenfilename(initialdir='Music', title='Choose a music', filetypes=(('mp3 files', '*.mp3'), ))
    song = song.replace('/home/eduardo/Escritorio/GawrGura_Player/Music/', "")
    song = song.replace('.mp3', "")
    song_box.insert(END, song)
    
canvas.place(x = 0, y = 0)
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(250, 250, image=entry_image_2)

song_box = Listbox(window, bg="white", fg="green", width=256, height=323)
song_box.pack(side="left", padx=20, pady=50)
song_box.config(relief="flat", bd=0, justify="left", font=("UD Digi Kyokasho NK-R", 24 * -1))

button_image_7 = ImageTk.PhotoImage(file=relative_to_assets("button_8.png"))
button_7 = canvas.create_image(32, 32, image=button_image_7, tag='Button_7')
canvas.tag_bind(button_7, "<Button>", lambda e: add_song())

def play_song():
    song = song_box.get(ACTIVE)
    song = f'/home/eduardo/Escritorio/GawrGura_Player/Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

button_image_6 = ImageTk.PhotoImage(file=relative_to_assets("button_5.png"))
button_6 = canvas.create_image(74, 32, image=button_image_6, tag='Button_6')
canvas.tag_bind(button_6, "<Button>", lambda e: play_song())

window.mainloop()