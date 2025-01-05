from views.register.register import Register
from views.home.home import Home
from dotenv import load_dotenv
import os

load_dotenv()

class SkeletonFunction:
    def __init__(self):
        '''This is a function class'''
    
    def convert_percentage(self, percentage, total_pixels):
        return (percentage/100) * total_pixels