from utils.function.skeleton.skeleton_function import SkeletonFunction
from components.window.window_property import WindowProperty
from utils.grid_structure import GridStructure
from views.register.register import Register
from views.home.home import Home
import customtkinter as ctk
import json
import os

class Skeleton(ctk.CTk, SkeletonFunction, GridStructure):
    def __init__(self):
        ctk.CTk.__init__(self)
        SkeletonFunction.__init__(self)
        self.set_window_properties()
        self.configure_grid()
        self.change_page()
        
    def set_window_properties(self):
        WindowProperty.title(self, os.getenv("TITLE"))
        WindowProperty.geometry(self, os.getenv("GEOMETRY"))
        WindowProperty.background(self, os.getenv("BG_1"))
    
    def configure_grid(self):
        self.configure_columns(self, 1, [{'weight': 1}])
        self.configure_rows(self, 1, [{'weight': 1}])
    
    def user_instance_created(self):
        try:
            file_path = os.path.join(os.getcwd(), 'user_instance', 'user_instance.json')
            with open(file_path, 'r', encoding='utf-8') as f:
                user_instance = json.load(f)
                f.close()
                if user_instance:
                    return True
                else:
                    return False
        except FileNotFoundError:
            return False

    def change_page(self):
        if self.user_instance_created():
            Home(self,  width=500, height=500, fg_color=os.getenv("BG_1")).put('grid', row=0, column=0, sticky='nsew')
        else:
            Register(self,  width=500, height=500, fg_color=os.getenv("BG_2")).put('grid', row=0, column=0)