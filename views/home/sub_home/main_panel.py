import customtkinter as ctk
from components.tab.tab_view import TabView
from utils.grid_structure import GridStructure
import os

class MainPanel(ctk.CTkFrame, GridStructure):
    def __init__(self, parent, **kwargs):
        ctk.CTkFrame.__init__(self, parent, **kwargs)
        GridStructure.__init__(self)
        self.configure_grid()

        self.add_tab_view(
            self,
            n=1,
            meta_data=[
                {
                    'fg_color': os.getenv("BG_2"),
                    'border_color': os.getenv("BG_5"),
                    'border_width': 1,
                    'width': 500, 'height': 500,
                    'segmented_button_fg_color': os.getenv("BG_4"),
                    'segmented_button_selected_color': os.getenv("BG_4"),
                    'segmented_button_selected_hover_color': os.getenv("BG_5"),
                    'segmented_button_unselected_color': os.getenv("BG_4"),
                    'segmented_button_unselected_hover_color': os.getenv("BG_5"),
                    'text_color': os.getenv("BG_6")
                }
            ],
            method='grid',
            position=[
                {'row': 0, 'column': 0}
            ]
        )

    def configure_grid(self):
        self.configure_columns(self, 1, {0: {'weight': 1}})
        self.configure_rows(self, 1, {0: {'weight': 1}})
    
    def add_tab_view(self, parent, **kwargs):
        for idx in range(kwargs['n']):
            TabView(parent, **kwargs['meta_data'][idx]).put(kwargs['method'], **kwargs['position'][idx])
    
    def put(self, method, **kwargs):
        getattr(self, method, None)(**kwargs)