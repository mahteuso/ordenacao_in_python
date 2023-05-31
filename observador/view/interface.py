from abc import ABC, abstractmethod

class InterfaceObserva(ABC):

    @abstractmethod
    def update(self, msg):
        ...