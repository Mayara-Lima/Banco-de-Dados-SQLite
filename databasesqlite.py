import sqlite3

banco = sqlite3.connect("biblioteca.db")
cursor = banco.cursor()

cursor.execute("CREATE TABLE autor(BI integer, nome text, apelidos text, estar_vivo text)")
cursor.execute("CREATE TABLE livro(isbn integer, título text, editorial text, ano_escrito text)")
cursor.execute("CREATE TABLE utilizador(BI integer, nome text, apelidos text, num_emprestimos text)")

cursor.execute("INSERT INTO autor VALUES(123456789, 'Mariana', 'Sousa Pereira', 'sim')")
cursor.execute("INSERT INTO autor VALUES(123567890, 'Augusto', 'Nobre', 'não')")
cursor.execute("INSERT INTO autor VALUES(457290277, 'Silvia', 'Pessoa', 'não')")

cursor.execute("INSERT INTO livro VALUES(246810, 'A montanha', 'Suzana Miranda', '2020-04-15')")
cursor.execute("INSERT INTO livro VALUES(846453, 'Eu', 'Clarice Barros', '1812-03-17')")
cursor.execute("INSERT INTO livro VALUES(768564, 'Mensagem', 'Sofia Mendonça', '1934-04-06')")

cursor.execute("INSERT INTO utilizador VALUES(912345678, 'Soraia', 'Correia Santos', 1)")
cursor.execute("INSERT INTO utilizador VALUES(982637369, 'Juliana', 'Nascimento Pascoal', 10)")
cursor.execute("INSERT INTO utilizador VALUES(912345678, 'Felipe', 'Alves Furtado', 11)")

banco.commit()

cursor.execute("SELECT * from autor")
autores = cursor.fetchall()
for autor in autores:
    print(autor)

cursor.execute("SELECT * from livro")
livros = cursor.fetchall()
for livro in livros:
    print(livro)

cursor.execute("SELECT * from utilizador")
utilizadores = cursor.fetchall()
for utilizador in utilizadores:
    print(utilizador)

cursor.execute("SELECT * from autor WHERE estar_vivo = 'Sim'")
autores_vivos = cursor.fetchall()
for autor in autores_vivos:
    print(autor)

cursor.execute("SELECT * from livro WHERE ano_escrito > 1900")
livros_modernos = cursor.fetchall()
for livro in livros_modernos:
    print(livro)

cursor.execute("SELECT nome from utilizador WHERE num_emprestimos > 10")
utilizador_ativo = cursor.fetchall()
for utilizador in utilizador_ativo:
    print(utilizador)

banco.close()
