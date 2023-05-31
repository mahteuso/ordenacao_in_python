from .interface import InterfaceObserva
from typing import Type

class Canal:
    def __init__(self):
        self.lista = []

    def segue_canal(self, seguidor: Type[InterfaceObserva]):
        self.lista.append(seguidor)

    def atualiza_seguidor(self, msg):
        for s in self.lista:
            s.update(msg)
