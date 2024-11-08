#from Aluno import Aluno
#from Livro import Livro
from Conta import ContaCorrente, ContaPoupanca, ContaSalario


c1 = ContaCorrente(123, 50)
c2 = ContaCorrente(987, 50)

c1.depositar(50)
c1.transferir(25, c2)
