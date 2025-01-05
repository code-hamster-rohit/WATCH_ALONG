from threading import Thread
from utils.function.register.request_function import RequestFunction
import os

class RegisterFunction:
    def __init__(self):
        '''This is a function class'''
        self.url = os.getenv("SERVER_URL") + '/user/create_instance'
    
    def create_user(self, user_data, parent, buttons):
        Thread(target = RequestFunction.send_post_request, args=(self.url, user_data, parent, buttons)).start()
        for button in buttons:
            button.configure(text='CREATING')
            button.configure(state='disabled')
            button.configure(text_color_disabled=os.getenv("BG_6"))