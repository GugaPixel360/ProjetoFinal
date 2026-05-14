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

#Cria conexao com o sql
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database='carrossel'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None

#def fazer denovo
def denovo():
    while True:
        print("=================")
        continuar = input("Deseja fazer mais alguma coisa? \n1 - Sim \n2 - Não \nDigite aqui: ")
        if continuar == "1":
            break
        elif continuar == "2":
            print("Muito obrigado por utilizar nossa loja.")
            exit()
        else:
            print("Valor inválido por favor responda com 1 ou 2.")
        print("=================")

# valida o id do docente que o usuario colocou 
def validar_id(id_docente):
    while True:
        if id_docente.strip() == "":
            print("Campo vazio!")
            continue

        if not id_docente.isdigit():
            print("Apenas números!")
            continue

        break

# valida a senha na hora do create 
def validar_senha(senha):
    while True:

        letra = any(caracter.isalpha() for caracter in senha)
        num = any(caracter.isdigit() for caracter in senha)
        carac = any(not caracter.isalnum() for caracter in senha)
 
        if len(senha) > 10 or len(senha) < 1:
            print("Coloque menos de 10 valores")
            continue
           
        if letra and num and carac:
            print("Senha valida")
            break
            
        else:
            print ("=================")
            if not letra:
                print ("Precisa de letra")
                

            if not num:
                print ("Precisa de numero")
                
                
            if not carac:
                print ("Precisa de caracter especial")
                
                

            print ("Tente denovo")
            print ("============")
            continue
            
# entra no login do docente 
def Entrar(id_docente, senha):
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

#read - table de docentes
def ler_docente():
    print ("=================")
    conn = criar_conexao()
    cursor = conn.cursor()
    
    cursor.execute("SELECT*FROM professor")

    resultado = cursor.fetchall()
    for linha in resultado:
        print (f"Código do docente: {linha[0]} | Nome: {linha[1]} | Função: {linha[2]}")

    cursor.close()
    conn.close()

    print ("=================")


#Print inicial
print("Bem vindo ao menu da escola Carrossel!\n" )


while True:
    op = input("Você já tem login?\n | 0 - Sair \n | 1 - Entrar \n | 2 - Criar login\n")

    match op:
        case "0":
            print ("Você saiu")
            break
        

        case "1":
            ler_docente()
            print("\33[31m===============\033[m")
            idf = input("Digite seu ID: ")
            Senhaf = input("Digite a sua senha: ")   
            print("\33[31m===============\033[m") 

            id_docente = validar_id() 
            Entrar(id_docente)

            match verificar_docente():

                #professor
                case 1:
                    print("\33[30m==== OLÁ PROFESSOR DIGITE A OPÇÃO QUE VOCÊ DESEJA ALTERAR====\033[m")
                    op = input("0 - Sair \n | 1 - Nota \n | 2 - Situação do aluno \n | 3 - Informações do aluno \n")

                    if op == 0:
                        print("Você saiu")
                        break

                    elif op == 1:
                        



                #coordenador
                case 2:
                #diretor
                case 3:
            
            
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

