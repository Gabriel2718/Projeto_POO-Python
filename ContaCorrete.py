class ContaCorrente(Conta):
    def __init__(self, numero, limiteCredito):
        super().__init__(numero)
        self.__limiteCredito = limiteCredito

    #getters
    def getLimiteCredito(self):
        return self.__limiteCredito

    #setters
    def setLimiteCredito(self, limiteCredito):
        self.__limiteCredito = limiteCredito
