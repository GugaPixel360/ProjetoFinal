#Sistema escolar

#Requisitos: interface no terminal, sistema deve ter validaçâo de campos, o sistema  teve ter permanencia de dados, CRUD MINIMO: Criar dados, Visualizar dados, Atualizar
#e deletar dados, deve permitir cadastrar alunos, registrar notas, calclr medias, mostar situacao e manter dados salvos no MySQL
#Funcionalidades minimas: Cadastrar aluno, Listar alunos, Remover alunos, Editar dados dos alunos, Adicionar/remover notas, Buscar aluno

#SCRIPT SQL:

# CREATE DATABASE IF NOT EXISTS Carrossel;

# USE carrossel;

# CREATE TABLE IF NOT EXISTS Alunos (
# nome_aluno VARCHAR (100) NOT NULL,
# idade_aluno INT NOT NULL,
# turma_aluno INT NOT NULL,
# matricula_ID INT AUTO_INCREMENT PRIMARY KEY,
# notasDoAluno INT
# );

# CREATE TABLE IF NOT EXISTS Situacao (
# notas_aluno_FK INT,
# media_aluno INT,
# situacao_aluno VARCHAR (100),
# matricula_FK_ID INT AUTO_INCREMENT PRIMARY KEY,
# FOREIGN KEY (Matricula_FK_ID) REFERENCES Alunos (Matricula_ID)

# );

# CREATE TABLE IF NOT EXISTS docente (
# id_docente int auto_increment primary key,
# nome_docente VARCHAR (100) NOT NULL,
# funcao_docente VARCHAR(20) NOT NULL,
# materia_docente VARCHAR(50) NOT NULL, 
# email_docente VARCHAR (50) NOT NULL,
# senha VARCHAR(10) NOT NULL
# );


import mysql.connector
from mysql.connector import Error

#Lista tendo todos as funcoes que um usuario pode ter no sistema
escolha_de_funcoes = ["professor", "coordenador", "diretor", "prof", "coord"]

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
            
#def de cadastro
def criar_login(Nome, Email, funcao, materia, Senha):
    ...

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
    resultado = cursor.fetchone()


    # se nao tiver docente
    if resultado is None or resultado[1] is None:
        print("=================")
        print("Nenhum usuário encontrado.")
        print("=================")
        return

    # print docente    
    for linha in resultado:
        print (f"Código do docente: {linha[0]} | Nome: {linha[1]} | Função: {linha[2]}")

    cursor.close()
    conn.close()

    print ("=================")

# verificacao da funcao do docente (se a funcao existe ou nao)
def verificar_funcao(funcao):
    funcao = funcao.lower()
    
    if not funcao == escolha_de_funcoes:
        return True

#retorna a funcao do docente
def verificar_docente(idf):
    while True:
        cursor = criar_conexao()

        busca = "SELECT * FROM professor WHERE funcaoDoProfessor = %s"

        cursor.execute(busca, (idf))

        resultado = cursor.fetchone()

        cursor.execute("SELECT * FROM professor WHERE funcaoDoProfessor = %s")

        oqvce = cursor.fetchall()

        for linha in oqvce:
            print("Fazendo busca...")

        if resultado:
            print(f"O valor '{idf}' FOI encontrado.")
            print(f"Você é {linha}")
        else:
            print(f"O valor '{idf}' NÃO foi encontrado.")
            continue

#excluir nota
def excluir_nota(id_nota):
    cursor = criar_conexao()
    sql = "DELETE FROM notas WHERE id = %s"
    cursor.execute(sql, (id_nota,))
    cursor.commit()

#Print inicial
print("Bem vindo ao menu da escola Carrossel!\n" )


while True:
    op = input("Você já tem login?\n | 0 - Sair \n | 1 - Entrar \n | 2 - Criar login\n | Escreva aqui: ")

    match op:
        case "0":
            print ("Você saiu")
            break
        
        case "1":
            if not ler_docente():
                print("Não ha nenhum usuário cadastrado")
                continue

            print("\33[31m===============\033[m")
            id_docente = input("Digite seu ID: ")
            Senhaf = input("Digite a sua senha: ")   
            print("\33[31m===============\033[m") 

            validar_id() 
            Entrar(id_docente)

            match verificar_docente(id_docente):

                #professor
                case 1:
                    print("\33[30m==== OLÁ PROFESSOR DIGITE A OPÇÃO QUE VOCÊ DESEJA ALTERAR====\033[m")
                    op = input("0 - Sair \n | 1 - Nota \n | 2 - Situação do aluno \n | 3 - Informações do aluno \n")

                    if op == "0":
                        print("Você saiu")
                        break

                    elif op == "1":
                            print("O que você gostaria de mexer?")
                            op = input("0 - Sair \n | 1 - adicionar \n | 2 - excluir")
                            
                            match op:
                                case 0:
                                    print("Você saiu")
                                    break

                                case 1:
                                     nota1 = input("Digite a 1° nota do alunos: ")
                                     nota2 = input("Digite a 2° nota do alunos: ")
                                     nota3 = input("Digite a 3° nota do alunos: ")

                                     print(f"Essas são as três notas do alunos \n 1° nota: {nota1} \n | 2° nota: {nota2} | 3° nota: {nota3}")


                                case 2:
                                    ler_notas()
                                    excluir_notas()

                                
                                case 3:
                                    ...

        
        case "2":
            print ("\33[34m===============\033[m")
            Nome = input("Digite seu nome completo: ").capitalize()
            Email = input("Digite a seu email: ")    
            funcao = input("Digite a sua função: ") 
            materia = input("Digite a sua matéria (Caso nao seja professor repita a sua função): ") 
            Senha = input("Crie a sua senha: ")    
            print("\33[31m===============\033[m")  
            verificar_funcao(funcao)
            validar_senha(Senha)
            criar_login(Nome, Email, funcao, materia, Senha)

        case _:
            print("Escolha uma das opções dadas")
            continue

