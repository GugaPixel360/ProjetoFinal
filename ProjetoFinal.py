#Sistema escolar

#Requisitos: interface no terminal, sistema deve ter validaçâo de campos, o sistema  teve ter permanencia de dados, CRUD MINIMO: Criar dados, Visualizar dados, Atualizar
#e deletar dados, deve permitir cadastrar alunos, registrar notas, calclr medias, mostar situacao e manter dados salvos no MySQL
#Funcionalidades minimas: Cadastrar aluno, Listar alunos, Remover alunos, Editar dados dos alunos, Adicionar/remover notas, Buscar aluno

#SCRIPT SQL:

#CREATE DATABASE IF NOT EXISTS Carrossel;

# USE carrossel;

# CREATE TABLE IF NOT EXISTS Alunos (
# NomeDoAluno VARCHAR (100) NOT NULL,
# IdadeDoAluno INT NOT NULL,
# TurmaDoAluno INT NOT NULL,
# Matricula_ID INT AUTO_INCREMENT PRIMARY KEY,
# NotasDoAluno INT PRIMARY KEY NOT NULL
# );

# CREATE TABLE IF NOT EXISTS Situacao (
# NotasDoAluno_FK INT PRIMARY KEY NOT NULL,
# MediaDoAluno INT NOT NULL,
# SituacaoDoAluno VARCHAR (100),
# Matricula_FK_ID INT AUTO_INCREMENT PRIMARY KEY,
# FOREIGN KEY (Matricula_FK_ID) REFERENCES Alunos (Matricula_ID),
# FOREIGN KEY (NotasDoAluno_FK) REFERENCES Alunos (NotasDoAluno)
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
            database='Carrossel'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None

Turma = []

def Matricula():
     while True:
        print("Vamos fazer a seua Matricula! por favor preencha todos os requisitos corretamente | Obrigado pela compreensão (;")
        print("================================================================================================================")
        conn = criar_conexao()
        if not conn:
            return
        
        cursor = conn.cursor()
         
        

        nome = input("Digite seu nome: ").strip()
        if nome.strip() == "":
            print("Vamo querer?")
            continue
        
        elif nome.isdigit():
            print("Não pode ser numero ;)")
            cursor.close()
            conn.close()
            continue
        
        idade = input("Digite sua idade: ").strip()
        if idade.strip() == "":
            print("Sério?")
            cursor.close()
            conn.close()
            continue
        
        elif idade <= "0":
            print("Sério?")
            cursor.close()
            conn.close()
            continue
        
        if not idade.isdigit():
            print("Não pode em letras ;)")
            cursor.close()
            conn.close()
            continue
        
        BtEmTurma = input("Em qual turma você gostaria de entrar? | Turmas: Turma01 |: ")
        if BtEmTurma == "01":

         Turma.append(nome)
         Turma.append(idade)
            
         cursor.execute(
        "INSERT INTO Alunos (NomeDoAluno, IdadeDoAluno, TurmaDoAluno) VALUES (%s, %s, %s)",
        (nome, idade, BtEmTurma)
        )
         
        else:
            print("Opção inválida")
        

        conn.commit()

        print(f"Aluno [{nome}] matriculado com sucesso!")

        cursor.close()
        conn.close()


        print("Obrigado por se matricular!")
        print("=================================================================================================================")
        Turma.append(nome)
        Turma.append(idade)
        break

go

Matricula()


while True:
    print("Bem vindo ao menu da escola Carrossel!\n" \
    "Digite oque gostarias de fazer?\n | 1 - Entrar (Apenas para professores) | 2 - Matricular aluno(a)\n | 3 - ")


