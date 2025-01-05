from threading import Thread
from utils.function.home.side_request_function import HomeRequestFunction
import os

class SidePanelFunction:
    def __init__(self):
        '''This is a function class'''
        self.get_method_url = os.getenv("SERVER_URL") + '/user/get_instance'
        self.patch_method_url = os.getenv("SERVER_URL") + '/user/update_instance'
    
    def get_user_details(self, query, entries):
        Thread(target = HomeRequestFunction.get_user_details, args=(self.get_method_url, query, entries)).start()
    
    def change_user_details(self, query, data, entries):
        for item in ['full_name', 'user_name']:
            if data[item] == None:
                data.pop(item)
        if len(data) == 0:
            return
        Thread(target = HomeRequestFunction.change_user_details, args=(self.patch_method_url, query, data, entries, self.get_method_url)).start()