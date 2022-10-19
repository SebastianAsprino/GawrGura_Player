
from googleapiclient.discovery import build

api_key = 'AIzaSyDx8fYaKQTVCdS14ywuE7Z3AJhJ4YprrTA'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='statistics',
        forUsername='sentdex'
    )
    
response = request.execute()

print(response)
