class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__contas = []

    #getters
    def getNome(self):
        return self.__nome

    def getCpf(self):
        return self.__cpf

    def getContas(self):
        return self.__contas

    #setters
    def setNome(self, nome):
        self.__nome = nome

    def setCpf(self, cpf):
        self.__cpf = cpf

    #method overload
    def setConta(self, conta):
        if isinstance(conta, Conta):
            self.getContas().append(conta)
    
    def setConta(self, conta, index):
        if isinstance(conta, Conta):
            self.getContas().insert(index, conta)
