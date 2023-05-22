# construtor

class Evento:
    def __init__(self, nome): #o construtor é iniciado com __init__
        self.nome = nome
        
    def altera_nome_evento(self, novo_nome):
        self.nome = novo_nome # self é igual o this