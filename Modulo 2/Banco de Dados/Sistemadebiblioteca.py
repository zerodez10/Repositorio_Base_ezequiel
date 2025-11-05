import sqlite3

Biblioteca = sqlite3.connect("Sistema de Biblioteca.db")

cursor = Biblioteca.cursor()

# cursor.execute("CREATE TABLE Emprestimo(Expedição date, recebimento date)")
# cursor.execute("INSERT INTO Emprestimo VALUES('24/03/2025', '31/03/2025') ")

# cursor.execute("CREATE TABLE Aluno(Aluno text,RA integer, Quantidade_de_Livros integer)")
# cursor.execute("INSERT INTO Aluno VALUES('Isaac', 643462, 1)")

# cursor.execute("CREATE TABLE Autor(Nome text, Tradutor text)")
# cursor.execute("INSERT INTO Autor VALUES('Albert einsten', 'Silvio Levy')")

# cursor.execute("CREATE TABLE Livro(Titulo text, Criação date, Quantidade_de_Paginas integer)")
# cursor.execute("INSERT INTO Livro VALUES('a Teoria da Relatividade', '01/08/1915', 195)")

# Biblioteca.commit()

# cursor.execute("Select * FROM Emprestimo")
cursor.execute("Select * FROM Aluno")
# cursor.execute("Select * FROM Autor")
# cursor.execute("Select * FROM Livro")
print(cursor.fetchall())
