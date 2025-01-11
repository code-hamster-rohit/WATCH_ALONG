import customtkinter as ctk
from utils.grid_structure import GridStructure
from components.top_level.top_level import TopLevel
from components.window.window_property import WindowProperty
from components.slider.slider import Slider
from components.button.button_property import ButtonProperty
from components.frame.frame import Frame
import os, vlc

class VideoPlayer(GridStructure):
    def __init__(self, parent=None, **kwargs):
        self.top_level = TopLevel.create(parent, **kwargs)
        self.instance = vlc.Instance()
        self.media = None
        self.media_player = self.instance.media_player_new()
        self.is_paused = False

        self.set_window_properties()
        self.configure_grid(self.top_level)

        self.add_frame(
            self.top_level,
            n = 3,
            meta_data = [
                {'fg_color': os.getenv("BG_3")},
                {'fg_color': os.getenv("BG_3")},
                {'fg_color': os.getenv("BG_3")}
            ],
            method = 'grid',
            position = [
                {'row': 0, 'column': 0, 'sticky': 'nsew'},
                {'row': 1, 'column': 0, 'sticky': 'nsew'},
                {'row': 2, 'column': 0, 'sticky': 'nsew'}
            ]
        )

        self.add_slider(
            self.frames[1],
            n = 1,
            meta_data = [
                {'orientation': 'horizontal', 'from_': 0, 'to': 1000, 'number_of_steps': 1000}
            ],
            method = 'grid',
            position = [
                {'row': 0, 'column': 0, 'sticky': 'nsew'}
            ]
        )

        self.add_inner_frame(
            self.frames[2],
            n = 1,
            meta_data = [
                {'fg_color': os.getenv("BG_3")}
            ],
            method = 'grid',
            position = [
                {'row': 0, 'column': 0, 'sticky': 'nsew'}
            ]
        )

        self.add_buttons(
            self.inner_frames[0],
            n = 3,
            meta_data = [
                {'text': 'Play'},
                {'text': 'Pause'},
                {'text': 'Stop'}
            ],
            method = 'grid',
            position = [
                {'row': 0, 'column': 0},
                {'row': 0, 'column': 1},
                {'row': 0, 'column': 2}
            ]
        )

        
    def set_window_properties(self):
        WindowProperty.title(self.top_level, os.getenv("TITLE") + ' PLAYER')
        WindowProperty.geometry(self.top_level, os.getenv("GEOMETRY"))
        WindowProperty.background(self.top_level, os.getenv("BG_1"))
    
    def configure_grid(self, parent):
        self.configure_columns(parent, 1, {0: {'weight': 1}})
        self.configure_rows(parent, 3, {0: {'weight': 98}, 1: {'weight': 1}, 2: {'weight': 1}})
    
    def add_frame(self, parent, **kwargs):
        self.frames = []
        for idx in range(kwargs['n']):
            fr = Frame.frame(parent, **kwargs['meta_data'][idx])
            Frame.put(fr, kwargs['method'], **kwargs['position'][idx])
            self.configure_columns(fr, 1, {0: {'weight': 1}})
            self.configure_rows(fr, 1, {0: {'weight': 1}})
            self.frames.append(fr)
    
    def add_slider(self, parent, **kwargs):
        self.sliders = []
        for idx in range(kwargs['n']):
            slider = Slider.slider(parent, **kwargs['meta_data'][idx])
            Slider.put(slider, kwargs['method'], **kwargs['position'][idx])
            slider.set(0)
            self.sliders.append(slider)
        
    def add_inner_frame(self, parent, **kwargs):
        self.inner_frames = []
        for idx in range(kwargs['n']):
            inner_frame = Frame.frame(parent, **kwargs['meta_data'][idx])
            Frame.put(inner_frame, kwargs['method'], **kwargs['position'][idx])
            self.configure_columns(inner_frame, 3, {0: {'weight': 1}, 1: {'weight': 1}, 2: {'weight': 1}})
            self.configure_rows(inner_frame, 1, {0: {'weight': 1}})
            self.inner_frames.append(inner_frame)
        
    
    def configure_grid_inner_frame(self, parent):
        self.configure_columns(parent, 3, {0: {'weight': 1}, 1: {'weight': 1}, 2: {'weight': 1}})
        self.configure_rows(parent, 1, {0: {'weight': 1}})
    
    def add_buttons(self, parent, **kwargs):
        self.buttons = []
        for idx in range(kwargs['n']):
            button = ButtonProperty.button(parent, **kwargs['meta_data'][idx])
            ButtonProperty.put(button, kwargs['method'], **kwargs['position'][idx])
            self.buttons.append(button)