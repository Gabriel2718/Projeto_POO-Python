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

    #operações básicas
    def sacar(self, valor):
        if(self.getSaldo() - valor >= 0):
            self.setSaldo(self.getSaldo() - valor)
            print("Saque realizado")
        else:
            print("Saldo insuficiente")

    def depositar(self, valor):
        self.setSaldo(self.getSaldo() + valor)
        print("Depósito realizado")

    def transferir(self, valor, destino):
        if(self.getSaldo() - valor >= 0):
            self.setSaldo(self.getSaldo() - valor)
            destino.setSaldo(destino.getSaldo() + valor)
            print("Saque realizado")
        else:
            print("Saldo insuficiente")
