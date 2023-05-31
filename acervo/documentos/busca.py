
from .tipo import Tipo
from typing import Type

class Busca:
    def __init__(self, tipo: Type[Tipo]) -> None:
        self.tipo = tipo


    def acervo(self, titulo):
       return self.tipo.acervo(titulo)

