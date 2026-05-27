CREATE DATABASE IF NOT EXISTS carrossel;

USE carrossel;

CREATE TABLE IF NOT EXISTS alunos (
nome_aluno VARCHAR (100) NOT NULL,
idade_aluno INT NOT NULL,
turma_aluno varchar (50) NOT NULL,
matricula_ID INT AUTO_INCREMENT PRIMARY KEy
);

CREATE TABLE IF NOT EXISTS notas (
nota1 INT,
nota2 INT,
nota3 INT,
nota4 INT,
media_aluno INT,
situacao_aluno VARCHAR (100),
matricula_FK_ID INT AUTO_INCREMENT PRIMARY KEY,
FOREIGN KEY (matricula_FK_ID) REFERENCES Alunos (matricula_ID)

);

CREATE TABLE IF NOT EXISTS professor (
id_docente int auto_increment primary key,  
nome_docente VARCHAR (100) NOT NULL,          
email_docente VARCHAR (50) NOT NULL,
senha VARCHAR (15) NOT NULL,
materia_docente VARCHAR (100) NOT NULL,
funcao_docente VARCHAR (50) NOT NULL
);

insert into alunos (nome_aluno, idade_aluno, turma_aluno) values ("josue", 15, "1ds");
insert into notas (nota1, nota2, nota3) values (7, 5, 8);

SELECT * FROM professor;

/*
SELECT nota1, nota2, nota3, nota4 FROM notas
INNER JOIN nota1, nota2, nota3, nota4 ON alunos;


Drop Database Carrossel;
