CREATE DATABASE IF NOT EXISTS carrossel;

USE carrossel;

CREATE TABLE IF NOT EXISTS alunos(
nome_aluno VARCHAR (100) NOT NULL,
idade_aluno INT NOT NULL,
turma_aluno varchar (20) NOT NULL,
matricula_ID INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS notas (
materia varchar (30),
nota1 float,
nota2 float,
nota3 float,
nota4 float,
media_aluno float,
situacao_aluno VARCHAR (100),

matricula_FK_ID INT,
FOREIGN KEY (matricula_FK_ID)
REFERENCES alunos(matricula_ID)

);

CREATE TABLE IF NOT EXISTS professor (
id_docente int auto_increment primary key,  
nome_docente VARCHAR (100) NOT NULL,          
email_docente VARCHAR (50) NOT NULL,
senha VARCHAR (15) NOT NULL,
materia_docente VARCHAR (100) NOT NULL,
funcao_docente VARCHAR (50) NOT NULL
);


INSERT INTO alunos(nome_aluno, idade_aluno, turma_aluno)
VALUES ("joberto", 14, "1DS");
INSERT INTO notas(
    nota1,
    nota2,
    nota3,
    matricula_FK_ID
)
VALUES (8, 7, 9, 1);
SELECT * FROM professor;
select * from alunos;
select *from notas;

/*
truncate table notas;

/*
Drop Database Carrossel;

