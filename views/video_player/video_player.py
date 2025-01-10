import customtkinter as ctk
from components.top_level.top_level import TopLevel
from components.window.window_property import WindowProperty
import os

class VideoPlayer():
    def __init__(self, parent=None, **kwargs):
        self.top_level = TopLevel.create(parent, **kwargs)
        self.set_window_properties()
        
    def set_window_properties(self):
        WindowProperty.title(self.top_level, os.getenv("TITLE") + ' PLAYER')
        WindowProperty.geometry(self.top_level, os.getenv("GEOMETRY"))
        WindowProperty.background(self.top_level, os.getenv("BG_1"))
    
    
