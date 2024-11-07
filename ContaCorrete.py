class ContaCorrente(Conta):
    def __init__(self, numero, limiteCredito):
        super().__init__(numero)
        self.__limiteCredito = limiteCredito
