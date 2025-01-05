import customtkinter as ctk
from views.home.sub_home.inner_side_panel import InnerSidePanel
from utils.grid_structure import GridStructure
from components.label.label_property import LabelProperty
import os

class SidePanel(ctk.CTkFrame, GridStructure):
    def __init__(self, parent, **kwargs):
        ctk.CTkFrame.__init__(self, parent, **kwargs)
        GridStructure.__init__(self)

        self.configure_grid()
        self.add_label(
            self,
            n=1,
            meta_data=[
                {'text': 'SETTINGS', 'font': ('Montserrat', 24), 'fg_color': os.getenv("BG_3"), 'text_color': os.getenv("BG_6")}
            ],
            method='grid',
            position=[
                {'row': 0, 'column': 0, 'sticky': 'nsew', 'padx': 50, 'pady': 50}
            ]
        )
        self.add_inner_side_panel(
            self,
            fg_color=os.getenv("BG_3")
        )

    def configure_grid(self):
        self.configure_columns(self, 1, {0: {'weight': 1}})
        self.configure_rows(self, 2, {0: {'weight': 1}, 1: {'weight': 1}})
    
    def add_label(self, parent, **kwargs):
        self.labels = []
        for idx in range(kwargs['n']):
            label = LabelProperty.label(parent, **(kwargs['meta_data'])[idx])
            LabelProperty.put(label, kwargs['method'], **(kwargs['position'])[idx])
            self.labels.append(label)
    
    def add_inner_side_panel(self, parent, **kwargs):
        InnerSidePanel(parent, **kwargs).put('grid', row=1, column=0, sticky='new')

    def put(self, method, **kwargs):
        getattr(self, method, None)(**kwargs)
    