from listeners import listener

class CommandListener(listener.Listener):
    filter:str

    def __init__(self, filter):
        super().__init__(filter)
    
