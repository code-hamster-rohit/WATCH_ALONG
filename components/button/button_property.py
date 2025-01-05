import customtkinter as ctk

class ButtonProperty:
    def __init__(self):
        '''This class contains the properties of the button'''
        
    @staticmethod
    def button(parent, **kwargs):
        return ctk.CTkButton(parent, **kwargs)
    
    @staticmethod
    def put(button, method, **kwargs):
        getattr(button, method, None)(**kwargs)