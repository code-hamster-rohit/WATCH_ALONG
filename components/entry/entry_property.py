import customtkinter as ctk

class EntryProperty:
    def __init__(self):
        '''Creates an entry widget'''
    
    @staticmethod
    def entry(parent, **kwargs):
        return ctk.CTkEntry(parent, **kwargs)

    @staticmethod
    def put(entry, method, **kwargs):
        getattr(entry, method, None)(**kwargs)