from abc import *

class GameImpl(metaclass = ABCMeta):
    @abstractmethod
    def getUserName(self):
        pass

    @abstractmethod
    def execute(self):
        pass