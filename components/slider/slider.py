import customtkinter as ctk

class Slider:

    @staticmethod
    def slider(parent, **kwargs):
        return ctk.CTkSlider(parent, **kwargs)
    
    @staticmethod
    def put(parent, method, **kwargs):
        getattr(parent, method, None)(**kwargs)