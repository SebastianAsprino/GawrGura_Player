from pygame import mixer

class playSong:
    #inicia el mixer
    mixer.init()
    #reproduce el archivo que se le proporcione
    def play_song(self, entrada):
        self.song = entrada
        self.song = f'{self.song}.mp3'
        mixer.music.load(self.song)
        mixer.music.play(loops=0)
