CREATE DATABASE IF NOT EXISTS carrossel;

USE carrossel;

CREATE TABLE IF NOT EXISTS alunos (
nome_aluno VARCHAR (100) NOT NULL,
idade_aluno INT NOT NULL,
turma_aluno INT NOT NULL,
matricula_ID INT AUTO_INCREMENT PRIMARY KEY,
);

CREATE TABLE IF NOT EXISTS notas (
notas_aluno INT,
media_aluno INT,
situacao_aluno VARCHAR (100),
matricula_FK_ID INT AUTO_INCREMENT PRIMARY KEY,
FOREIGN KEY (matricula_FK_ID) REFERENCES Alunos (matricula_ID)

);

CREATE TABLE IF NOT EXISTS professor (
id_docente int auto_increment primary key,  
nome_docente VARCHAR (100) NOT NULL,
funcao_docente VARCHAR (50) NOT NULL,             
email_docente VARCHAR (50) NOT NULL,
senha VARCHAR (15) NOT NULL,
materia_docente VARCHAR (100) NOT NULL
);

SELECT notas_aluno FROM notas
INNER JOIN notas_aluno ON alunos;

/*
Drop Database Carrossel;

