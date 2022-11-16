from listeners import listener
from telegram.ext import filters

class MessageListener(listener.Listener):
    filter:filters

    def __init__(self, filter):
        super().__init__(filter)
    
    