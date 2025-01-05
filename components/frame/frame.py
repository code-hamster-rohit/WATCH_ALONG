import customtkinter as ctk

class Frame:
    def __init__(self):
        '''This class is used to create a frame widget'''
    
    @staticmethod
    def frame(parent, **kwargs):
        return ctk.CTkFrame(parent, **kwargs)
    
    @staticmethod
    def put(parent, method, **kwargs):
        getattr(parent, method, None)(**kwargs)