import customtkinter as ctk
from utils.grid_structure import GridStructure
from views.home.sub_home.side_panel import SidePanel
from views.home.sub_home.main_panel import MainPanel
import os

class Home(ctk.CTkFrame, GridStructure):
    def __init__(self, parent, **kwargs):
        ctk.CTkFrame.__init__(self, parent, **kwargs)
        GridStructure.__init__(self)
        self.configure_grid()
        self.add_frame(
            self,
            n=2,
            panel_name=['side_panel', 'main_panel'],
            meta_data=[
                {'fg_color': os.getenv("BG_2")},
                {'fg_color': os.getenv("BG_3")}
            ]
        )

    def configure_grid(self):
        self.configure_columns(self, 2, {0: {'weight': 1}, 1: {'weight': 9}})
        self.configure_rows(self, 1, {0: {'weight': 1}})
    
    def add_frame(self, parent, **kwargs):
        for idx, panel_name in enumerate(kwargs['panel_name']):
            if panel_name == 'side_panel':
                SidePanel(parent, **kwargs['meta_data'][idx]).put('grid', row=0, column=0, sticky='nsew')
            else:
                MainPanel(parent, **kwargs['meta_data'][idx]).put('grid', row=0, column=1, sticky='nsew', padx=(50, 50))

    def put(self, method, **kwargs):
        getattr(self, method, None)(**kwargs)