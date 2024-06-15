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

#ALTER TABLE `schema-principal`.`departames` 
#ADD COLUMN `Recurso` VARCHAR(45) NULL AFTER `nome`,
#ADD COLUMN `Ti` VARCHAR(50) NOT NULL AFTER `Recurso`,
#ADD COLUMN `Matketing` VARCHAR(100) NOT NULL AFTER `Ti`,
#CHANGE COLUMN `nome` `nome` TEXT(100) NOT NULL ,
#DROP PRIMARY KEY,
#ADD PRIMARY KEY (`idepe`, `Recurso`, `Matketing`);

# Muda o nome das variaves dentro da tabela----
#select idepe as codigodeidentificação, nome as areas
#from departames 
#group by idepe;,

#Mostra os Funcionarios ---------------------
#select Funcionarios.none as funcionario, Funcionarios.cargo, Funcionarios.salarios, Departamentos.none as departamento 
#from Funcionarios
#join Departamentos on Funcionarios.departamento_id = departamento.id 

#Mostra o cargo ----------------
#select Funcionarios.nome as funcionario, funcionarios.cargo as cargo, Departamentos.nome as Departamento 
#from Funcionarios
#join Departamentos on Funcionarios.departamento_id = Departamentos.id where Departamentos.nome = 'T.I'

#select  nome from livro where autor = 'J. K. Rowling' and Paginas > 400  

