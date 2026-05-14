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

def validar_id():
    while True:
        id_docente = input("Qual seu ID?").strip().isdigit() #4


        if not id_docente.isdigit():
            print("Apenas números!")
            continue

        if id_docente.strip() == "":
            print("Campo vazio!")
            continue

        return id_docente #4

def Entrar(id_docente):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "SELECT * FROM professor WHERE id_docente = %s AND senha = %s"
    valores = (id_docente, senha)
    cursor.execute(sql, valores)
    resultado = cursor.fetchone()  
   
    cursor.close()
    conn.close()
 
    if not resultado:
        print (f"------------")
        print("Senha não encontrada")
        print (f"------------")
        return False
    else:
        return True

def validar_senha():
    while True:

        letra = any(caracter.isalpha() for caracter in senha)
        num = any(caracter.isdigit() for caracter in senha)
        carac = any(not caracter.isalnum() for caracter in senha)
 
        if len(senha) > 10 or len(senha) < 1:
            print("Coloque menos de 10 valores")
            continue
           
 
 
        if letra and num and carac:
            print("senha valida")
            return senha
            

        else:
            print ("=================")
            if not letra:
                print ("precisa de letra")
                

            if not num:
                print ("precisa de numero")
                
                
            if not carac:
                print ("precisa de caracter especial")
                
                

            print ("tente denovo")
            print ("============")
            continue
            

            
            
            
            
        




print("Bem vindo ao menu da escola Carrossel!\n" )


while True:
    op = input("Você já tem login?\n | 0 - Sair \n | 1 - Entrar \n | 2 - Criar login\n")

    match op:
        case "0":
            print ("Você saiu")
            break

        case "1":
            print("\33[31m===============\033[m")
            Nomef = input("Digite seu ID: ")
            Senhaf = input("Digite a sua senha: ")   
            print("\33[31m===============\033[m") 
            
            id_docente = validar_id() 
            Entrar(id_docente)
        case "2":
            print ("\33[34m===============\033[m")
            Nomef = input("Digite seu nome completo: ")
            Senhaf = input("Digite a sua senha: ")    
            Emailf = input("Digite a seu email: ")    
            Funcaof = input("Digite a sua função: ") 
            print("\33[31m===============\033[m")  

        case _:
            print("Escolha uma das opções dadas")
            continue





