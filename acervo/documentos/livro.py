
class Livro:

    def __init__(self):
        self.livro = {}
        self.acervo = []


    def insere_livro(self, nome, ano, paginas):
        self.livro.update({f'{nome}': f'páginas: {paginas}, ano: {ano}'})
        self.insere_acervo()

    def insere_acervo(self):
        if len(self.acervo) > 0:
            self.acervo.pop()
        self.acervo.append(self.livro)

    def busca_livro(self, titulo):
        titulo.lower().strip()
        if self.livro[titulo]:
            return f'Nome: {titulo}, {self.livro[titulo]}'
        return 'Não temos esse título em nossa base de dados'


    def __repr__(self):
        return f'{[livro for livro in self.acervo]}'

