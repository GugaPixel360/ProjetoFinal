CREATE DATABASE IF NOT EXISTS carrossel;

USE carrossel;

CREATE TABLE IF NOT EXISTS alunos (
nome_aluno VARCHAR (100) NOT NULL,
idade_aluno INT NOT NULL,
turma_aluno INT NOT NULL,
matricula_ID INT AUTO_INCREMENT PRIMARY KEY,
notas_aluno INT
);

CREATE TABLE IF NOT EXISTS situacao (
notas_aluno_FK INT,
media_aluno INT,
situacao_aluno VARCHAR (100),
matricula_FK_ID INT AUTO_INCREMENT PRIMARY KEY,
FOREIGN KEY (Matricula_FK_ID) REFERENCES Alunos (Matricula_ID)

);

CREATE TABLE IF NOT EXISTS professor (
id_docente int auto_increment primary key,  
nome_docente VARCHAR (100) NOT NULL,
funcao_docente VARCHAR (50) NOT NULL,             
email_docente VARCHAR (50) NOT NULL,
senha VARCHAR (15) NOT NULL,
materia_docente VARCHAR (100) NOT NULL
);


/*
Drop Database Carrossel;

