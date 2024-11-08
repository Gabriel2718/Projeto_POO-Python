class ContaSalario(Conta):
    def __init__(self, numero, rendimento):
        super().__init__(numero)
        self.__rendimento = rendimento

    #getters
    def getRendimento(self):
        return self.__rendimento

    #setters
    def setRendimentos(self, rendimento):
        self.__rendimento = rendimento
