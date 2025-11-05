import sqlite3

Clinica = sqlite3.connect("Clinica médica.db")

cursor = Clinica.cursor()

cursor.execute("CREATE TABLE Medico(Nome text, idade integer)")
cursor.execute("INSERT INTO Medico VALUES('João pinto', '35') ")

cursor.execute("CREATE TABLE Especialidade(Especialidade text)")
cursor.execute("INSERT INTO Especialidade VALUES('Pediatria')")

cursor.execute("CREATE TABLE Pacientes(Nome text, Idade integer)")
cursor.execute("INSERT INTO Pacientes VALUES('Jonathan anta', '6')")

cursor.execute("CREATE TABLE Consultas(Médico_responsável text, Paciente date, Data date, Horario hour)")
cursor.execute("INSERT INTO Consultas VALUES('João pinto', 'Jonathan anta', '21/10/2025', '15:45:00')")

Clinica.commit()

cursor.execute("Select * FROM Medico")
cursor.execute("Select * FROM Especialidade")
cursor.execute("Select * FROM Pacientes")
cursor.execute("Select * FROM Consultas")
print(cursor.fetchall())
