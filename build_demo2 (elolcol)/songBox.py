from PIL import ImageTk, Image
from pathlib import Path
from tinytag import TinyTag
import io
import webbrowser
from api_youtube import *
from tkinter import *
from tkinter import Entry, PhotoImage, Listbox, filedialog, messagebox
from PIL import Image, ImageTk
import tkinter as tk
import psutil
from pathlib import Path
from pygame import mixer

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

mixer.init()

class songBox:
    """clase de testeo"""
    def __init__ (self):
        self.songbox = tk.Tk()
        self.songbox.geometry("500x500")
        self.canvas = tk.Canvas(self.songbox, bg = "#FFFFFF", height = 800, width = 800, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(250, 250, image=self.entry_image_2)
        self.button_image_7 = ImageTk.PhotoImage(file=relative_to_assets("button_8.png"))
        self.button_7 = self.canvas.create_image(32, 32, image=self.button_image_7, tag='Button_7')
        self.canvas.tag_bind(self.button_7, "<Button>", lambda e: self.add_song())
        self.button_image_6 = ImageTk.PhotoImage(file=relative_to_assets("button_5.png"))
        self.button_6 = self.canvas.create_image(74, 32, image=self.button_image_6, tag='Button_6')
        self.canvas.tag_bind(self.button_6, "<Button>", lambda e: self.play_song())  
        self.song_box = Listbox(self.songbox, bg="white", fg="green", width=256, height=323)
        self.song_box.pack(side="left", padx=20, pady=50)
        self.song_box.config(relief="flat", bd=0, justify="left", font=("UD Digi Kyokasho NK-R", 24 * -1))
        self.songbox.mainloop()
    
    def add_song(self):
        self.user_info = psutil.users()
        self.user = self.user_info[0][0]
        self.song = filedialog.askopenfilenames(initialdir='Music', title='Choose a music', filetypes=(('mp3 files', '*.mp3'), ))
        
        self.dir=(Path(__file__).parent.absolute())

        for song in self.song:
            song = song.replace(str(self.dir), "")
            song = song.replace('.mp3', "")
            self.song_box.insert(END, song)
    
    def play_song(self):
        self.song = self.song_box.get(ACTIVE)
        self.song = f'{self.song}.mp3'
        mixer.music.load(self.song)
        mixer.music.play(loops=0)
        #print(self.song)
        #webbrowser.open(self.song)

if __name__ == '__main__':
    sonbox = songBox()