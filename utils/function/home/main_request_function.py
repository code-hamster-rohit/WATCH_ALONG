from views.video_player.video_player import VideoPlayer
import requests

class MainRequestFunction:

    @staticmethod
    def create_room(url, data):
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                VideoPlayer()
            else:
                return response.status_code
        except requests.exceptions.RequestException as e:
            return 500
    
    @staticmethod
    def join_room(url, query, data):
        try:
            response = requests.patch(url, params=query, json=data)
            if response.status_code == 200:
                VideoPlayer()
            else:
                return response.status_code
        except requests.exceptions.RequestException as e:
            return 500