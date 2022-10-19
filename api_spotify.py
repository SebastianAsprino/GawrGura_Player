import pandas as pd 
import spotipy 
 
""" Necesitamos los modulos de spotipy y pandas. Si nos los tenemos, los instalaremos escribiendo en la consola:
    pip install spotipy
    pip install pandas
"""sp = spotipy.Spotify() 
from spotipy.oauth2 import SpotifyClientCredentials 
 cid ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
 sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
 sp.trace=False
# Obtenemos información de la playlist de Spotify
playlist = sp.user_playlist("***usuario***", "***codigoplaylist***", fields="tracks,next")
tracks = playlist["tracks"] 
songs = tracks["items"]
