from abc import ABC, abstractmethod

class SystemModule(ABC):

    @abstractmethod
    def update(self):
        pass