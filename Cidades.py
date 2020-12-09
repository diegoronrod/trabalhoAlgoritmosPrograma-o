class Cidades:
    def __init__(self, nome, estado, qtcasos):
        self.nome = nome
        self.estado = estado
        self.qtcasos = qtcasos

    def get_nome(self):
        return self.nome

    def get_qtcasos(self):
        return self.qtcasos

    def set_qtcasos(self, qtcasos):
        self.qtcasos = qtcasos

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def atualiza(self, qtnova):
        self.qtcasos += qtnova
        self.estado.atualizaest(qtnova)

    def __str__(self):
        return str(self.nome.upper()) + str(self.estado) + str(self.qtcasos)
