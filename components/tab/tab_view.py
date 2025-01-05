import customtkinter as ctk
from utils.grid_structure import GridStructure
from views.home.sub_home.inner_main_panel import InnerMainPanel
from components.frame.frame import Frame
import os

class TabView(ctk.CTkTabview, GridStructure):
    def __init__(self, parent, **kwargs):
        ctk.CTkTabview.__init__(self, parent, **kwargs)
        GridStructure.__init__(self)
        self.add_tab(
            self,
            n=2,
            room_type=[
                'JOIN ROOM',
                'CREATE ROOM'
            ],
        )
        self.add_frame(
            parent=[self.tab('JOIN ROOM'),self.tab('CREATE ROOM')],
            n=2,
            meta_data=[
                {'fg_color': os.getenv("BG_3")},
                {'fg_color': os.getenv("BG_3")}
            ],
            method='grid',
            position=[
                {'row': 0, 'column': 0, 'sticky': 'nsew', 'padx': 50, 'pady': 50},
                {'row': 0, 'column': 0, 'sticky': 'nsew', 'padx': 50, 'pady': 50}
            ]
        )
        InnerMainPanel([self.frames[0], self.frames[1]])
    
    def add_tab(self, parent, **kwargs):
        for idx in range(kwargs['n']):
            parent.add(kwargs['room_type'][idx])
            self.configure_columns(parent.tab(kwargs['room_type'][idx]), 1, {0: {'weight': 1}})
            self.configure_rows(parent.tab(kwargs['room_type'][idx]), 1, {0: {'weight': 1}})
    
    def add_frame(self, parent, **kwargs):
        self.frames = []
        for idx in range(kwargs['n']):
            fr = Frame.frame(parent[idx], **kwargs['meta_data'][idx])
            Frame.put(fr, kwargs['method'], **kwargs['position'][idx])
            self.frames.append(fr)

    def put(self, method, **kwargs):
        getattr(self, method, None)(**kwargs)