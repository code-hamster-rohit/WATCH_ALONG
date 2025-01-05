from utils.grid_structure import GridStructure
from utils.function.home.main_panel_function import MainPanelFunction
from components.entry.entry_property import EntryProperty
from components.button.button_property import ButtonProperty
from components.label.label_property import LabelProperty
from threading import Thread
import requests
import random
import json
import os

class InnerMainPanel(GridStructure, MainPanelFunction):
    def __init__(self, frames):
        GridStructure.__init__(self)
        MainPanelFunction.__init__(self)

        with open(os.path.join(os.getcwd(), 'user_instance', 'user_instance.json'), 'r', encoding='utf-8') as f:
            self.system_id = json.load(f)
            f.close()
        
        self.entries, self.buttons = {}, []
        self.frames = frames
        self.configure_grid()
        self.add_entry(
            'JOIN ROOM',
            self.frames[0],
            n=1,
            meta_data=[
                {'width': 200, 'height': 40, 'placeholder_text': 'ROOM CODE', 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_3"), 'text_color': os.getenv("BG_6"), 'border_color': os.getenv("BG_5"), 'border_width': 1}
            ],
            method='grid',
            position=[{'row': 0, 'column': 0, 'sticky': 'ew', 'padx': 50, 'pady': (50, 0)}]
        )
        self.add_button(
            self.frames[0],
            n=1,
            meta_data=[
                {'width': 100, 'height': 40, 'text': 'JOIN', 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_4"), 'text_color': os.getenv("BG_6"), 'hover_color': os.getenv("BG_5"), 'border_color': os.getenv("BG_5"), 'border_width': 1,
                'command': lambda: self.join_room(
                    {
                        'room_id': self.entries['JOIN_ROOM'][0].get()
                    },
                    {
                        'participant': self.system_id
                    }
                )}
            ],
            method='grid',
            position=[{'row': 1, 'column': 0, 'sticky': 'n'}],
        )
        Thread(target = self.get_room_ids, args = ()).start()
        self.add_entry(
            'CREATE ROOM',
            self.frames[1],
            n=2,
            meta_data=[
                {'width': 200, 'height': 40, 'placeholder_text': 'FILE PATH', 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_3"), 'text_color': os.getenv("BG_6"), 'border_color': os.getenv("BG_5"), 'border_width': 1},
                {'width': 200, 'height': 40, 'placeholder_text': 'MAX PARTICIPANTS', 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_3"), 'text_color': os.getenv("BG_6"), 'border_color': os.getenv("BG_5"), 'border_width': 1}
            ],
            method='grid',
            position=[
                {'row': 1, 'column': 0, 'sticky': 'sew', 'padx': 50, 'pady': (0, 10)},
                {'row': 2, 'column': 0, 'sticky': 'new', 'padx': 50, 'pady': (10, 0)}
            ]
        )
        self.add_button(
            self.frames[1],
            n=1,
            meta_data=[
                {'width': 100, 'height': 40, 'text': 'CREATE', 'font': ('Montserrat', 12), 'fg_color': os.getenv("BG_4"), 'text_color': os.getenv("BG_6"), 'hover_color': os.getenv("BG_5"), 'border_color': os.getenv("BG_5"), 'border_width': 1,
                'command': lambda: self.create_room(
                    {
                        'room_id': self.room,
                        'capacity': self.entries['CREATE_ROOM'][1].get(),
                        'participants': [self.system_id]
                    }
                )}
            ],
            method='grid',
            position=[{'row': 3, 'column': 0, 'sticky': 'n'}],
        )
    
    def configure_grid(self):
        for frame in self.frames:
            if frame == 'JOIN ROOM':
                self.configure_columns(frame, 1, {0: {'weight': 1}})
                self.configure_rows(frame, 2, {0: {'weight': 1}, 1: {'weight': 1}})
            else:
                self.configure_columns(frame, 1, {0: {'weight': 1}})
                self.configure_rows(frame, 4, {0: {'weight': 1}, 1: {'weight': 1}, 2: {'weight': 1}, 3: {'weight': 1}})
    
    def add_entry(self, type, parent, **kwargs):
        entries = []
        for idx in range(kwargs['n']):
            entry = EntryProperty.entry(parent, **(kwargs['meta_data'])[idx])
            EntryProperty.put(entry, kwargs['method'], **(kwargs['position'])[idx])
            entries.append(entry)
        if type == 'JOIN ROOM':
            self.entries['JOIN_ROOM'] = entries
        else:
            self.entries['CREATE_ROOM'] = entries
    
    def add_button(self, parent, **kwargs):
        for idx in range(kwargs['n']):
            button = ButtonProperty.button(parent, **(kwargs['meta_data'])[idx])
            ButtonProperty.put(button, kwargs['method'], **(kwargs['position'])[idx])
            self.buttons.append(button)
    
    def add_label(self, parent, **kwargs):
        self.labels = []
        for idx in range(kwargs['n']):
            label = LabelProperty.label(parent, **(kwargs['meta_data'])[idx])
            LabelProperty.put(label, kwargs['method'], **(kwargs['position'])[idx])
            self.labels.append(label)
    
    def get_room_ids(self):
        try:
            response = requests.get(os.getenv("SERVER_URL") + '/room/list')
            if response.status_code == 200:
                self.room_ids = response.json()['room_ids']
                self.room = self.create_room_id()
                self.add_label(
                    self.frames[1],
                    n=1,
                    meta_data=[
                        {'text': f'ROOM ID - {self.room}', 'font': ('Montserrat', 24), 'fg_color': os.getenv("BG_3"), 'text_color': os.getenv("BG_6")}
                    ],
                    method='grid',
                    position=[{'row': 0, 'column': 0, 'sticky': 'nsew'}]
                )
            else:
                return response.status_code
        except requests.exceptions.RequestException as e:
            return 500
    
    def create_room_id(self):
        random_int = random.randint(100000, 999999)
        if str(random_int) not in self.room_ids:
            return str(random_int)
        else:
            return self.create_room_id()