from .MainView import MainView
from .screens import Lappy486

class StrongBadEmail(object):
    def __init__(self):
        self.main_view = MainView()
    
    def start(self):
        self.main_view.start()