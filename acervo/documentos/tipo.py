from .seriado import Seriado
from .filme import Filme
from .livro import Livro

class Tipo():
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo.lower().strip()
        self.livro = Livro()
        self.filme = Filme()
        self.seriado = Seriado()


    def criar_acervo(self, nome: str, ano: int, duracao=None) -> None:
        if self.tipo == 'livro':
            self.livro.insere_livro(nome, ano, duracao)
        elif self.tipo == 'filme':
            self.filme.insere_filme(nome, ano, duracao)
        else:
            self.seriado.insere_seriado(nome, ano, duracao)



    def exporta_acervo(self):

        if self.tipo == 'filme':
            return self.filme
        elif self.tipo == 'seriado':
            return self.seriado
        elif self.tipo == 'livro':
            return self.livro
        return 'O título procurado não existe em nossa base de dados'


    def acervo(self, titulo):
        if self.tipo == 'filme':
            return self.filme.busca_filme(titulo)
        elif self.tipo == 'livro':
            return self.livro.busca_livro(titulo)
        elif self.tipo == 'seriado':
            return self.seriado.busca_seriado(titulo)
        else:
            raise Exception('Não temos esse ipo em nossa base de dados')


