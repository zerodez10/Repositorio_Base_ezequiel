import sqlite3

banco = sqlite3.connect("banco.db")

cursor = banco.cursor()

# cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)")

# cursor.execute("INSERT INTO pessoas VALUES('Isaac', 17, 'isaac@gmail.com')")
# cursor.execute("INSERT INTO pessoas VALUES('José', 15, 'jose@gmail.com')")
# cursor.execute("INSERT INTO pessoas VALUES('Ezequiel', 15, 'Ezequiel@gmail.com')")
# cursor.execute("INSERT INTO pessoas VALUES('Kauã', 15, 'kaua@gmail.com')")
# cursor.execute("INSERT INTO pessoas VALUES('pedro', 16, 'pedro@gmail.com')")

# cursor.execute("DELETE FROM pessoas WHERE nome = 'pedro'")

# cursor.execute('UPDATE pessoas SET nome = "Pedro" WHERE nome = "José"')

banco.commit()
cursor.execute("Select * FROM pessoas")
print(cursor.fetchall())
