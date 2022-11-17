"""
# shows artist info for a URN or URL 

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Radiohead'
  
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
result = sp.search(search_str)
pprint.pprint(result)
"""
import spotipy
class api_spotify:
    """iniciar sesion usuario y buscar canciones para reproducir"""
    
    
## prueba de que cambiar el nombre no altero git
