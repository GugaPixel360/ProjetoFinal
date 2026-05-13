CREATE DATABASE IF NOT EXISTS Carrossel;

USE carrossel;

CREATE TABLE IF NOT EXISTS Alunos (
NomeDoAluno VARCHAR (100) NOT NULL,
IdadeDoAluno INT NOT NULL,
TurmaDoAluno INT NOT NULL,
Matricula_ID INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Situacao (
NotasDoAluno INT NOT NULL,
MediaDoAluno INT NOT NULL,
SituacaoDoAluno VARCHAR (100),
Matricula_FK_ID INT AUTO_INCREMENT PRIMARY KEY,
FOREIGN KEY (Matricula_FK_ID) REFERENCES Alunos (Matricula_ID)
);

Select * From Alunos;
Select * From Situacao;



Drop Database Carrossel;

