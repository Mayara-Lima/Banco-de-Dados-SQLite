Base de Dados com SQLite


O SQLite é uma base de dados relacional de código aberto, é leve e possui uma velocidade excelente. 
Funciona muito bem em aplicações diversas, principalmente em websites de tráfego médio e sistemas mobile.

Neste projeto foi criada uma base de dados chamada biblioteca com os seguintes dados fictícios:

• Autor: com bi, nome, apelido(s) e se está vivo ou não.

• Livro: com isbn, título, editorial, ano em que foi escrito)

• Utilizador: com bi, nome, apelido(s), número de empréstimos na biblioteca)


Foram feitas as seguintes consultas:

• Listar todos os autores
• Listar todos os livros
• Listar todos os utilizadores
• Listar todos os autores que estejam vivos (CLÁUSULA WHERE)
• Listar todos os livros que tenham sido escritos posteriormente a 1900
• Listar todos os utilizadores que levaram mais de 10 livros e filtrar pelo
nome.


Ao conferir no DB Browser temos o resultado:

![image](https://user-images.githubusercontent.com/109659867/229108933-5358010c-e221-4745-ba07-15b0f3d9dee9.png)

