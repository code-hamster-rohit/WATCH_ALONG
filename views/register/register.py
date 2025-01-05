import customtkinter as ctk
from utils.function.register.register_function import RegisterFunction
from utils.grid_structure import GridStructure
from components.entry.entry_property import EntryProperty
from components.button.button_property import ButtonProperty
import os

class Register(ctk.CTkFrame, GridStructure, RegisterFunction):
    def __init__(self, parent, **kwargs):
        '''This class creates the register view'''
        ctk.CTkFrame.__init__(self, parent, **kwargs)
        GridStructure.__init__(self)
        RegisterFunction.__init__(self)
        self.configure_grid()
        self.add_entry(
            self,
            n=3,
            meta_data=[
                {'placeholder_text': 'FULL NAME', 'width': 200, 'height': 40, 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_3"), 'border_color': os.getenv("BG_5"), 'border_width': 1, 'text_color': os.getenv("BG_6")},
                {'placeholder_text': 'USERNAME', 'width': 200, 'height': 40, 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_3"), 'border_color': os.getenv("BG_5"), 'border_width': 1, 'text_color': os.getenv("BG_6")},
                {'placeholder_text': 'PASSWORD', 'width': 200, 'height': 40, 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_3"), 'border_color': os.getenv("BG_5"), 'border_width': 1, 'text_color': os.getenv("BG_6")}
            ],
            method='grid',
            position=[
                {'row': 0, 'column': 0, 'padx': 50, 'pady': (50, 10)},
                {'row': 1, 'column': 0, 'padx': 50, 'pady': 10},
                {'row': 2, 'column': 0, 'padx': 50, 'pady': 10}
            ]
        )
        self.add_button(
            self,
            n=1,
            meta_data=[
                {'text': 'CREATE', 'width': 100, 'height': 40, 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_4"), 'text_color': os.getenv("BG_6"), 'border_color': os.getenv("BG_5"), 'border_width': 1, 'hover_color': os.getenv("BG_5"),
                'command':lambda: self.create_user({
                    'full_name': self.entries[0].get(),
                    'user_name': self.entries[1].get(),
                    'password': self.entries[2].get()
                }, parent, self.buttons)}
            ],
            method='grid',
            position=[
                {'row': 3, 'column': 0, 'padx': 50, 'pady': (30, 50)}
            ]
        )
    
    def configure_grid(self):
        self.configure_columns(self, 1, {0: {'weight': 1}})
        self.configure_rows(self, 1, {0: {'weight': 1}})
    
    def put(self, method, **kwargs):
        getattr(self, method, None)(**kwargs) 
    
    def add_entry(self, parent, **kwargs):
        self.entries = []
        for idx in range(kwargs['n']):
            entry = EntryProperty.entry(parent, **(kwargs['meta_data'])[idx])
            EntryProperty.put(entry, kwargs['method'], **(kwargs['position'])[idx])
            self.entries.append(entry)
    
    def add_button(self, parent, **kwargs):
        self.buttons = []
        for idx in range(kwargs['n']):
            button = ButtonProperty.button(parent, **(kwargs['meta_data'])[idx])
            ButtonProperty.put(button, kwargs['method'], **(kwargs['position'])[idx])
            self.buttons.append(button)


