
class Seriado:

    def __init__(self):
        self.seriado = {}
        self.acervo = []


    def insere_seriado(self, nome, ano, temporadas):
        self.seriado.update({f'{nome}': f'ano: {ano}, temporadas:  {temporadas}'})
        self.insere_acervo()

    def insere_acervo(self):
        if len(self.acervo) > 0:
            self.acervo.pop()
        self.acervo.append(self.seriado)

    def busca_seriado(self, titulo):
        titulo.lower().strip()
        if self.seriado[titulo]:
            return f'Nome: {titulo}, {self.seriado[titulo]}'
        return 'Não temos esse título em nossa base de dados'

    def __repr__(self):
        return f'{[seriado for seriado in self.acervo]}'
