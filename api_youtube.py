"""
from googleapiclient.discovery import build

api_key = 'AIzaSyAv17jQbyO0zjmK4op2yDJ7RLExHLcigNs'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='statistics',
        forUsername='sentdex'
    )
    
response = request.execute()

print(response)"""
class api_youtube:
    """Es el api de youtube inicia sesion"""
    
    
    pass


