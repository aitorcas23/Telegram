import abc

class DataBase:
    @abc.abstractmethod
    def save(self, item):
        pass
    
    @abc.abstractmethod
    def get(self, key):
        pass