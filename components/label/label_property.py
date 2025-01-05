import customtkinter as ctk

class LabelProperty:
    def __init__(self):
        '''Creates a label widget'''
    
    @staticmethod
    def label(parent, **kwargs):
        return ctk.CTkLabel(parent, **kwargs)

    @staticmethod
    def put(label, method, **kwargs):
        getattr(label, method, None)(**kwargs)