class WindowProperty:
    def __init__(self):
        '''This class contains the properties of the window'''
        
    @staticmethod
    def title(window, title):
        window.title(title)
    
    @staticmethod
    def geometry(window, geometry):
        window.geometry(geometry)
    
    @staticmethod
    def background(window, bg_color):
        window.configure(fg_color=bg_color)