class Estados:
    def __init__(self, nomeest, sigla, qtest):

        self.nomeest = nomeest
        self.sigla    = sigla
        self.qtest   = qtest

    def get_nomeest(self):
        return self.nomeest

    def get_qtest(self):
        return self.qtest

    def get_sigla(self):
        return self.sigla

    def atualizaest(self, qtest):
        self.qtest += qtest

    def __str__(self):
        return str(self.nomeest.upper()) + str(self.sigla.upper()) + str(self.qtest)


