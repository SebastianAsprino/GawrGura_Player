
from googleapiclient.discovery import build

api_key = 'AIzaSyAv17jQbyO0zjmK4op2yDJ7RLExHLcigNs'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='statistics',
        forUsername='sentdex'
    )
    
response = request.execute()

print(response)
