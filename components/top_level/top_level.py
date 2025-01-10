import customtkinter as ctk

class TopLevel():
    
    @staticmethod
    def create(parent, **kwargs):
        return ctk.CTkToplevel(parent, **kwargs)