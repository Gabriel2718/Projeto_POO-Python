class Conta:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo

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
