from pytube import YouTube
import os
class api_youtube:
    #descarga la cancion de los servidores de youtube a partir de un link
    def recibe_url(self,entrada):
        self.url = entrada
        print(self.url)

        self.video = YouTube(self.url)
        print('Title: ', self.video.title)
        self.descargar(self.video)

    def descargar(self,vi):
        self.out_path = vi.streams.filter(only_audio=True).first().download(output_path='./Music')
        name = os.path.splitext(self.out_path)
        print('..........descargando la cancion..........')
        os.rename(self.out_path, name[0]+'.mp3')
        print('.........la cancion ya se descargo........')




