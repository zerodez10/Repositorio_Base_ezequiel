import sqlite3
import flet as ft

# cursor.execute("CREATE TABLE IF NOT EXISTS Matriculas (id INTEGER PRIMARY KEY AUTOINCREMENT, id_aluno INTEGER, id_curso INTEGER, id_professor INTEGER, data TEXT, FOREIGN KEY (id_aluno) REFERENCES Alunos(id), FOREIGN KEY (id_curso) REFERENCES Cursos(id), FOREIGN KEY (id_professor) REFERENCES Professores(id))")

def main(page: ft.Page):
    Titulo = ft.Text("Banco de dados")
    
    def criar_tabela_alunos(e):
        valor_1 = tabela.value
        conexao = sqlite3.connect("fabrica_programadores.db")
        cursor = conexao.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {valor_1} (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       Nome Text not null, 
                       Idade Text not null, 
                       Cidade Text not null""")
        conexao.commit()
        conexao.close()
    def criar_tabela_professores(e):
        valor_2 = tabela.value
        conexao = sqlite3.connect("fabrica_programadores.db")
        cursor = conexao.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {valor_2} (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       Nome Text not null, 
                       Idade Text not null""")
        conexao.commit()
        conexao.close()
    def criar_tabela_Cursos(e):
        valor_3 = tabela.value
        conexao = sqlite3.connect("fabrica_programadores.db")
        cursor = conexao.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {valor_3} (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       Nome Text not null, 
                       Carga_horaria Text not null, 
                       Preço Text not null""")
        conexao.commit()
        conexao.close()
        
    botão_criar_banco = ft.ElevatedButton("Criar Tabela com nome ", on_click = criar_tabela_alunos)
    tabela = ft.TextField(Label = "Escreva o nome do seu banco de dados")
    page.add(Titulo, 
             tabela, 
             botão_criar_banco)

ft.app(target=main)



# Etapa 2 – Inserção de Dados
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Ezequiel', 15, 'Barueri')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('José', 15, 'Osasco')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Isaac', 15, 'Barueri')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Juan', 15, 'Carapicuiba')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Kauã', 15, 'Surubim PE')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Davi', 15, 'Barueri')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Arthur felix', 16, 'Barra mansa RJ')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Gustavo alessandro', 16, 'Barueri')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Isabelle Luisa', 15, 'Itapevi')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Isabelle Eduarda', 15, 'Não identificado')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Kethleen', 15, 'Barueri')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Rebeca', 15, 'Itapevi')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Roberta', 15, 'Guarulhos')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Vitória', 15, 'Barueri')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Stefany', 15, 'Barueri')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Maisa', 15, 'São paulo')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Carioca teste delete', 15, 'São paulo')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Gustavo Souza', 17, 'Barueri')")
# cursor.execute ("INSERT INTO Alunos (Nome, Idade, Cidade) VALUES ('Pedro', 15, 'Barueri')")

# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preço) VALUES ('Excel basico', 20, 100.00)")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preço) VALUES ('Python Básico', 40, 500.00)")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preço) VALUES ('Python Intermediario', 60, 750.00)")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preço) VALUES ('Python Avançado', 80, 1000.00)")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preço) VALUES ('Java Básico', 40, 700.00)")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preço) VALUES ('Java Intermediário', 60, 1000.00)")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preço) VALUES ('Java Avançado', 80, 1200.00)")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preço) VALUES ('Administrador de banco de dados', 120, 2500.00)")

# cursor.execute("INSERT INTO Professores (Nome, Idade) VALUES ('Ricardo', 25)")
# cursor.execute("INSERT INTO Professores (Nome, Idade) VALUES ('Marli', 29)")
# cursor.execute("INSERT INTO Professores (Nome, Idade) VALUES ('Jorge', 36)")
# cursor.execute("INSERT INTO Professores (Nome, Idade) VALUES ('Alcir', 34)")
# cursor.execute("INSERT INTO Professores (Nome, Idade) VALUES ('Maria cleide', 30)")
# cursor.execute("INSERT INTO Professores (Nome, Idade) VALUES ('Camilla', 27)")
# cursor.execute("INSERT INTO Professores (Nome, Idade) VALUES ('Ana lucia', 34)")

# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (1, 8, 7, '30/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (2, 4, 7, '12/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (3, 7,3, '30/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (4, 5,4, '12/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (5, 2,7, '12/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (6, 1,1, '30/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (7, 3,1, '06/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (8, 2,2, '06/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (9, 4,5, '30/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (10, 6,3, '06/04/2012')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (11, 8,2, '24/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (12, 8,4, '24/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (13, 3,4, '13/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (14, 5,7,'30/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (15, 4,3,'13/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (16, 1,2,'13/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (17, 2,1,'30/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (18, 5,3,'06/04/2025')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, id_professor, data) VALUES (19, 2,6,'06/04/2025')")

# Etapa 3 – Consultas com SELECT
# cursor.execute("SELECT Cidade FROM Alunos")
# cursor.execute("SELECT carga_horaria from Cursos WHERE carga_horaria >=40 ORDER BY preço")
# cursor.execute("SELECT Alunos.Nome, Cursos.Nome FROM Matriculas INNER JOIN Alunos ON id_aluno = Alunos.id INNER JOIN Cursos ON id_curso = Cursos.id")
# cursor.execute("SELECT COUNT(id_aluno) FROM Matriculas WHERE id_curso = 2")
# print(cursor.fetchall())


# Etapa 4 – UPDATE
# cursor.execute("UPDATE cursos SET preço = preço * 1.10  WHERE carga_horaria >= 80")
# cursor.execute("UPDATE Alunos SET Cidade = 'Rio de Janeiro' WHERE Nome = 'Carioca teste delete'")

# # Etapa 5 – DELETE
# cursor.execute("DELETE FROM Alunos WHERE id = 17")
# cursor.execute("DELETE FROM Matriculas WHERE id_aluno = 17")
# cursor.execute("DELETE FROM Cursos WHERE preço <= 200.00")

# # Etapa 6 – INSERT Extra
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preço) VALUES ('Inteligência Artificial', 60, 1200.00)")

# Etapa 7 – Relatório Final
# cursor.execute("SELECT Cursos.Nome AS Curso, Cursos.preço AS Preço, COUNT(Matriculas.id_aluno) AS Total_Aluno FROM Cursos LEFT JOIN Matriculas ON Matriculas.id_curso = Cursos.id GROUP BY Cursos.id, Cursos.Nome, Cursos.preço ORDER BY Cursos.preço DESC LIMIT 5")
# print(cursor.fetchall())
# Fabrica.commit()
