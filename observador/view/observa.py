from .interface import InterfaceObserva

class Observa(InterfaceObserva):
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def update(self, msg):
        print(f'{self.nome} escuta: {msg}')

    def __repr__(self):
        return f'Sou eu {self.nome} -> seu seguidor : {Observa}'
