from Aluno import Aluno
from Livro import Livro

aluno1 = Aluno("Aluno1", "Sobrenome1", 123654)
aluno2 = Aluno("Aluno2", "Sobrenome2", 987456)

livro1 = Livro("Python - Cap. 1", "Guido Van Rossum", 11111)
livro2 = Livro("Java - Cap. 1", "James Gosling", 11112)

print("\nAlunos cadastrados:")
aluno1.imprimir()
aluno2.imprimir()

print("\nLivros cadastrados:")
livro1.imprimir()
livro2.imprimir()
