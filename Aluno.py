class Aluno:
    def __init__(self, nome, sobrenome, ra):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__ra = ra
        
    #getters
    def getNome(self):
        return self.__nome
        
    def getSobrenome(self):
        return self.__sobrenome
        
    def getRa(self):
        return self.__ra
        
    #setters
    def setNome(self, nome):
        self.__nome = nome
        
    def setSobrenome(self, sobrenome):
        self.__sobrenome = sobrenome
        
    def setRa(self, ra):
        self.__ra = ra
        
    
    def imprimir(self):
        print("Nome: ", self.getNome(), "\nSobrenome: ", self.getSobrenome(), "\nRA: ", self.getRa(), "\n")
        