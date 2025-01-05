from threading import Thread
from utils.function.home.main_request_function import MainRequestFunction
import os

class MainPanelFunction:
    def __init__(self):
        '''This is a function class'''
        self.create_url = os.getenv("SERVER_URL") + '/room/create'
        self.join_url = os.getenv("SERVER_URL") + '/room/join'
    
    def create_room(self, data):
        Thread(target = MainRequestFunction.create_room, args=(self.create_url, data)).start()
    
    def join_room(self, query, data):
        Thread(target = MainRequestFunction.join_room, args=(self.join_url, query, data)).start()