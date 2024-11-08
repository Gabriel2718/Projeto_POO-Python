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
        self.__numero = numero

    def setSaldo(self, saldo):
        self.__saldo = saldo

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
            if isinstance(destino, Conta):
                self.setSaldo(self.getSaldo() - valor)
                destino.setSaldo(destino.getSaldo() + valor)
                print("Transferência realizada")
        else:
            print("Saldo insuficiente")

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

class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero)

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