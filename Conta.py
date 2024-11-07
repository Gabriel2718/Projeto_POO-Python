class Conta:
    def __init__(self, numero):
        self.__numero = numero
        self.__saldo = 0.0

    #getters
    def getNumero(self):
        return self.__numero

    def getSaldo(self):
        return self.__saldo

    #setters
    def setNumero(self, numero):
        return self.__numero = saldo

    def setSaldo(self, saldo):
        return self.__saldo = saldo
