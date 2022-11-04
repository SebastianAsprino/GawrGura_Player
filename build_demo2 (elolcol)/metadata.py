from PIL import Image, ImageDraw, ImageOps
import io
from tinytag import TinyTag
import os
from tkinter import filedialog

song = filedialog.askopenfilename(initialdir='Music', title='Choose a music', filetypes=(('mp3 files', '*.mp3'), ))

AudioMetadata = TinyTag.get(song, image=True)

im = AudioMetadata.get_image()

pi = Image.open(io.BytesIO(im))

pi.save("build_demo1/assets/cover.png")

def round_edges(im, radius):
    mask = Image.new("L", (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)

    alpha = Image.new("L", im.size, 255)
    w, h = im.size

    alpha.paste(mask.crop((0, 0, radius, radius)), box=(0, 0))
    alpha.paste(mask.crop((0, radius, radius, radius * 2)), box=(0, h - radius))
    alpha.paste(mask.crop((radius, 0, radius * 2, radius)), box=(w - radius, 0))
    alpha.paste(mask.crop((radius, radius, radius * 2, radius * 2)), box=(w - radius, h - radius))

    im.putalpha(alpha)
    return im

if __name__ == "__main__":
    with Image.open('build_demo1/assets/cover.png') as im:

        im = im.convert("RGBA")

        rounded_im = round_edges(im, 100)
        rounded_im.save('build_demo1/assets/cover_rounded.png')

if os.path.exists('build_demo1/assets/cover.png'):
    os.remove('build_demo1/assets/cover.png')

        