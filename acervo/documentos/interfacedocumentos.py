from abc import ABC, abstractmethod

class Documentos(ABC):

    @abstractmethod
    def insere_documento(self):
        ...

