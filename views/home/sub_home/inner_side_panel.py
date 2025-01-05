import customtkinter as ctk
from utils.grid_structure import GridStructure
from utils.function.home.side_panel_function import SidePanelFunction
from components.entry.entry_property import EntryProperty
from components.button.button_property import ButtonProperty
from components.dialog.dialog_box import DialogBox
import json
import os

class InnerSidePanel(ctk.CTkFrame, GridStructure, SidePanelFunction):
    def __init__(self, parent, **kwargs):
        ctk.CTkFrame.__init__(self, parent, **kwargs)
        GridStructure.__init__(self)
        SidePanelFunction.__init__(self)

        with open(os.path.join(os.getcwd(), 'user_instance', 'user_instance.json'), 'r', encoding='utf-8') as f:
            self.system_id = json.load(f)
            f.close()

        self.configure_grid()
        self.add_entry(
            self,
            n=3,
            meta_data=[
                {'placeholder_text': 'FULL NAME', 'width': 200, 'height': 40, 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_3"), 'border_color': os.getenv("BG_5"), 'border_width': 1, 'text_color': os.getenv("BG_6"), 'state': 'disabled'},
                {'placeholder_text': 'USERNAME', 'width': 200, 'height': 40, 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_3"), 'border_color': os.getenv("BG_5"), 'border_width': 1, 'text_color': os.getenv("BG_6"), 'state': 'disabled'},
                {'placeholder_text': 'PASSWORD', 'width': 200, 'height': 40, 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_3"), 'border_color': os.getenv("BG_5"), 'border_width': 1, 'text_color': os.getenv("BG_6"), 'state': 'disabled'}
            ],
            method='grid',
            position=[
                {'row': 0, 'column': 0, 'pady': (50, 10)},
                {'row': 1, 'column': 0, 'pady': 10},
                {'row': 2, 'column': 0, 'pady': 10}
            ]
        )
        self.add_button(
            self,
            n=1,
            meta_data=[
                {'text': 'CHANGE', 'width': 100, 'height': 40, 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_4"), 'text_color': os.getenv("BG_6"), 'border_color': os.getenv("BG_5"), 'border_width': 1, 'hover_color': os.getenv("BG_5"),
                'command': lambda: self.change_user_details(
                    {
                        'system_id': self.system_id,
                    },
                    {
                        'full_name': DialogBox(text = 'NEW FULL NAME', title = 'CHANGE FULL NAME', entry_fg_color = os.getenv("BG_2"), entry_text_color = os.getenv("BG_6"), entry_border_color = os.getenv("BG_5"), fg_color = os.getenv("BG_2"), button_fg_color = os.getenv("BG_4"), button_hover_color = os.getenv("BG_5"), button_text_color = os.getenv("BG_6")).get_input(),
                        'user_name': DialogBox(text = 'NEW USERNAME', title = 'CHANGE USERNAME', entry_fg_color = os.getenv("BG_2"), entry_text_color = os.getenv("BG_6"), entry_border_color = os.getenv("BG_5"), fg_color = os.getenv("BG_2"), button_fg_color = os.getenv("BG_4"), button_hover_color = os.getenv("BG_5"), button_text_color = os.getenv("BG_6")).get_input(),
                    },
                    self.entries
                )}
            ],
            method='grid',
            position=[
                {'row': 3, 'column': 0, 'pady': (30, 50)}
            ]
        )

        self.get_user_details({
            'system_id': self.system_id
        }, self.entries)
    
    def configure_grid(self):
        self.configure_columns(self, 1, {0: {'weight': 1}})
        self.configure_rows(self, 1, {0: {'weight': 1}})

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
    
    def put(self, method, **kwargs):
        getattr(self, method, None)(**kwargs)