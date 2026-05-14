CREATE DATABASE IF NOT EXISTS Carrossel;

USE carrossel;

CREATE TABLE IF NOT EXISTS Alunos (
nome_Aluno VARCHAR (100) NOT NULL,
idade_Aluno INT NOT NULL,
turma_Aluno INT NOT NULL,
matricula_ID INT AUTO_INCREMENT PRIMARY KEY,
notas_Aluno INT
);

CREATE TABLE IF NOT EXISTS Situacao (
notas_Aluno_FK INT,
media_Aluno INT,
situacao_Aluno VARCHAR (100),
matricula_FK_ID INT AUTO_INCREMENT PRIMARY KEY,
FOREIGN KEY (Matricula_FK_ID) REFERENCES Alunos (Matricula_ID)

);

CREATE TABLE IF NOT EXISTS professor (
id_docente int auto_increment primary key,  
nome_professor VARCHAR (100) NOT NULL,
funcao_Professor INT NOT NULL,             
email_Professor INT NOT NULL,
senha VARCHAR (15) NOT NULL,
materia_Professor VARCHAR (100) NOT NULL
);


/*
Drop Database Carrossel;

