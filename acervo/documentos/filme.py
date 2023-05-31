
class Filme:

    def __init__(self):
        self.filme = {}
        self.acervo = []


    def insere_filme(self, nome, ano, duracao):
        self.filme.update({f'{nome}': f'ano: {ano}, duração: {duracao}'})
        self.insere_acervo()

    def insere_acervo(self):
        if len(self.acervo) > 0:
            self.acervo.pop()
        self.acervo.append(self.filme)

    def busca_filme(self, titulo):
        titulo.lower().strip()
        if self.filme[titulo]:
            return f'Nome: {titulo}, {self.filme[titulo]}'
        return 'Não temos esse título em nossa base de dados'

    def __repr__(self):
        return f'{[filme for filme in self.acervo]}'


