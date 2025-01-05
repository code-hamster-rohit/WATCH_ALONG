class GridStructure:
    def __init__(self):
        '''This class is responsible for setting the grid structure of the window.'''
    
    def configure_columns(self, parent, n, properties):
        for idx in range(n):
            parent.grid_columnconfigure(idx, **properties[idx])
    
    def configure_rows(self, parent, n, properties):
        for idx in range(n):
            parent.grid_rowconfigure(idx, **properties[idx])