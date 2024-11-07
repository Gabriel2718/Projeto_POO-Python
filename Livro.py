class Livro:
    def __init__(self, nome, autor, codigo):
        self.__nome = nome
        self.__autor = autor
        self.__codigo = codigo
        
    #getters
    def getNome(self):
        return self.__nome
        
    def getAutor(self):
        return self.__autor
        
    def getCodigo(self):
        return self.__codigo
        
    #setters
    def setNome(self, nome):
        self.__nome = nome
        
    def setAutor(self, autor):
        self.__autor = autor
        
    def setCodigo(self, codigo):
        self.__codigo = codigo
        
        
    def imprimir(self):
        print("Nome: ", self.getNome(), "\nAutor: ", self.getAutor(), "\nCódigo: ", self.getCodigo(), "\n")
        