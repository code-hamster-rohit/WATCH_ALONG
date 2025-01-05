import customtkinter as ctk

class DialogBox(ctk.CTkInputDialog):
    def __init__(self, **kwargs):
        ctk.CTkInputDialog.__init__(self, **kwargs)