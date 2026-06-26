CREATE DATABASE IF NOT EXISTS carrossel;

USE carrossel;

CREATE TABLE IF NOT EXISTS alunos (
nome_aluno VARCHAR (100) NOT NULL,
idade_aluno INT NOT NULL,
turma_aluno varchar (50) NOT NULL,
matricula_ID INT AUTO_INCREMENT PRIMARY KEy
);

CREATE TABLE IF NOT EXISTS notas (
nota1 decimal (4,2),
nota2 decimal (4,2),
nota3 decimal (4,2),
nota4 decimal (4,2),
media_aluno decimal (4,2),
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

SELECT * FROM professor;
SELECT * FROM alunos;
SELECT * FROM notas;


/*
drop database carrossel;

