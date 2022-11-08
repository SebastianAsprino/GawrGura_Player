import pygame
from tkinter import filedialog
pygame.mixer.init()
song = filedialog.askopenfilename(initialdir='Music', title='Choose a music', filetypes=(('mp3 files', '*.mp3'), ))
pygame.mixer.music.load(song)
pygame.mixer.music.play(loops=0)