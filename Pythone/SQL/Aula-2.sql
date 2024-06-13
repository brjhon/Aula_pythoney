#select * from livro order by Paginas desc

#INSERT INTO livro (nome, autor, edicao, Paginas) VALUES
#('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', '1', 1200),
#('Harry Potter e a Câmara Secreta', 'J. K. Rowling', '2', 1200),
#('Harry Potter e o Prisioneiro de Azkaban', 'J. K. Rowling', '3', 1200)

#select nome from livro where Paginas > 500 

#CREATE TABLE alunos (
#    id INT AUTO_INCREMENT PRIMARY KEY,
#    nome VARCHAR(100) NOT NULL,
#    data_nascimento DATE,
#    genero ENUM('Masculino', 'Feminino', 'Outro'),
#    email VARCHAR(100) UNIQUE,
#    telefone VARCHAR(15),
#    endereco VARCHAR(255)
#);

#select  nome from livro where autor = 'J. K. Rowling' and Paginas > 400  



