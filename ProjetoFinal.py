#Sistema escolar

#Requisitos: interface no terminal, sistema deve ter validaçâo de campos, o sistema  teve ter permanencia de dados, CRUD MINIMO: Criar dados, Visualizar dados, Atualizar
#e deletar dados, deve permitir cadastrar alunos, registrar notas, calclr medias, mostar situacao e manter dados salvos no MySQL
#Funcionalidades minimas: Cadastrar aluno, Listar alunos, Remover alunos, Editar dados dos alunos, Adicionar/remover notas, Buscar aluno

#SCRIPT SQL:

# CREATE DATABASE IF NOT EXISTS Carrossel;

# USE carrossel;

# CREATE TABLE IF NOT EXISTS Alunos (
# NomeDoAluno VARCHAR (100) NOT NULL,
# IdadeDoAluno INT NOT NULL,
# TurmaDoAluno INT NOT NULL,
# Matricula_ID INT AUTO_INCREMENT PRIMARY KEY
# );

# CREATE TABLE IF NOT EXISTS Situacao (
# NotasDoAluno INT NOT NULL,
# MediaDoAluno INT NOT NULL,
# SituacaoDoAluno VARCHAR (100),
# Matricula_FK_ID INT AUTO_INCREMENT PRIMARY KEY,
# FOREIGN KEY (Matricula_FK_ID) REFERENCES Alunos (Matricula_ID)
# );

# Select * From Alunos;
# Select * From Situacao;



# Drop Database Carrossel;

import mysql.connector
from mysql.connector import Error


def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database='ProjetoFinal_Escola-Carrossel'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None
    


    
Turmas = []

def validar_nome(nome):
   conn = criar_conexao()
   if not conn:
        return

  
   if nome == "":
      return False

   for usuari in nome:
      if usuari >= "0" and usuari <= "9":
         return False
   return True


def validar_idade(idade):
   if idade == "":
      return False

   for usuari in idade:
      if usuari <= "0" or usuari >= "9":
         return False
   return True



  
print("Bem vindo ao sistema de matriculas da escola Carrossel!!")



