CREATE DATABASE IF NOT EXISTS Carrossel;

USE carrossel;

CREATE TABLE IF NOT EXISTS Alunos (
nomeDoAluno VARCHAR (100) NOT NULL,
idadeDoAluno INT NOT NULL,
turmaDoAluno INT NOT NULL,
matricula_ID INT AUTO_INCREMENT PRIMARY KEY,
notasDoAluno INT,
oqvce VARCHAR (100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Situacao (
notasDoAluno_FK INT,
mediaDoAluno INT,
situacaoDoAluno VARCHAR (100),
matricula_FK_ID INT AUTO_INCREMENT PRIMARY KEY,
FOREIGN KEY (Matricula_FK_ID) REFERENCES Alunos (Matricula_ID)

);

CREATE TABLE IF NOT EXISTS professor (
id_docente int auto_increment primary key,
nomeDoprofessor VARCHAR (100) NOT NULL,
funcaoDoProfessor INT NOT NULL,
emailDoProfessor INT NOT NULL,
senha VARCHAR(15) NOT NULL,
);


/*
Drop Database Carrossel;

