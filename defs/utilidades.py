import mysql.connector
from mysql.connector import Error

from defs.validacoes import *


#DEFs BASICOS!!!!


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

#bloco de prinst para erro
def erro():
    print("---------------------------")
    print("*Ocorreu um erro tente novamente*")
    print("---------------------------")

#def fazer denovo
def denovo():
    while True:
        print("=================")
        continuar = input("Deseja fazer mais alguma coisa? \n1 - Sim \n2 - Não \nDigite aqui: ")

        if continuar.strip() == "":
            print("Campo vazio!")
            continue

        elif continuar == "1":
            break

        elif continuar == "2":
            print("Sério? Ok né...")
            exit()
        else:
            print("Valor inválido por favor responda com 1 ou 2.")
        print("=================")



#DEFs DE LOGIN E CREATE                  


#def de cadastro
def criar_login(Nome, Email, funcao, materia, senha):
    conn = criar_conexao()

    if conn is None:
        print("Falha na conexão")
        return

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO professor (nome_docente, email_docente, funcao_docente, materia_docente, senha) VALUES (%s, %s, %s, %s, %s)",
        (Nome, Email, funcao, materia, senha)
    )

    conn.commit()

    print("Usuário cadastrado com sucesso!")

    cursor.close()
    conn.close()

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

#def adicionar nota
def adicionar_nota(matricula):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    
    nota1 = input("Digite a nota: ")

    
    validar_nota(nota1)

    valores = (nota1, matricula)
    sql = ("INSERT INTO pedidos (matricula_FK_ID, notas_aluno_FK) VALUES (%s, %s)", (matricula, nota1))
    cursor.execute (sql, valores)
    conexao.commit()

    print("Nota adicionada com sucesso!")

    cursor.close()
    conexao.close()

#Cria a media de um aluno    
def media():
    while True:

        conn = criar_conexao()
        cursor = conn.cursor()

        id_aluno = int(input("Digite a matricula do aluno"))
        validar_aluno(id_aluno)

        if id_aluno.strip() == "":
            print("Campo vazio!")
            continue

        elif not id_aluno.isdigit():
            print("Apenas numeros!")
            continue

        ver = ...
    
    


        sql = "SELECT nota1, nota2, nota3, nota4 FROM notas WHERE matricula_ID = %s"
        cursor.execute(sql, (id_aluno,))

        resultado = cursor.fetchone()


        cursor.close()
        conn.close()


        if resultado:
            nota1, nota2, nota3, nota4 = resultado    
            media = (nota1 + nota2 + nota3 + nota4) / 4
        
            print(f"Notas do aluno {id_aluno}: {nota1}, {nota2}, {nota3}, {nota4}")
            print(f"Média final: {media}")
        
        
            if media >= 7.0:
                print("Status: Aprovado")
            else:
                print("Status: Recuperação")
        else:
            print(f"Nenhuma nota encontrada para o aluno com ID {id_aluno}.")


#DEFs LER


#read - table de docentes
def ler_docente():
    print ("=================")
    conn = criar_conexao()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM professor")
    resultado = cursor.fetchall()


    # se nao tiver docente
    if resultado is None:
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

#ler os alunos com todas as informaçoes
def ler_alunos_completo():
    conexao = criar_conexao()

    if conexao is None:
        print("Erro ao conectar com o banco!")
        return

    cursor = conexao.cursor()

    sql = "SELECT * FROM alunos"
    cursor.execute(sql)

    resultado = cursor.fetchall()

    if not resultado:
        print("======================")
        print("Nenhum aluno cadastrado")
        print("======================")
    else:
        print("======================")
        print("LISTA DE ALUNOS")
        print("======================")

        for aluno in resultado:
            print(
                f"Nome: {aluno[0]} | "
                f"Matrícula: {aluno[3]} | "
                f"Idade: {aluno[1]} | "
                f"Turma: {aluno[2]} | "
            )

    cursor.close()
    conexao.close()

#ler alunos - informaçoes basicas
def ler_alunos():
    conexao = criar_conexao()

    if conexao is None:
        print("Erro ao conectar com o banco!")
        return

    cursor = conexao.cursor()

    sql = "SELECT * FROM alunos"
    cursor.execute(sql)

    resultado = cursor.fetchall()

    if not resultado:
        print("======================")
        print("Nenhum aluno cadastrado")
        print("======================")
    else:
        print("======================")
        print("LISTA DE ALUNOS")
        print("======================")

        for aluno in resultado:
            print(
                f"Nome: {aluno[0]} | "
                f"Matrícula: {aluno[3]} | "
            )

    cursor.close()
    conexao.close()

#retorna a funcao do docente
def ler_funcao(id_docente):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "SELECT * FROM professor WHERE id_docente = %s"

    cursor.execute(sql, (id_docente,))

    resultado = cursor.fetchone()


    for linha in resultado:
        funcao_docente = linha

    if resultado:
        print(f"Seja bem vindo(a) {funcao_docente}")
        match funcao_docente:
            case "professor":
                return 1
            case "coordenador":
                return 2
            case "diretor":
                return 3

    else:
        print(f"O valor '{id_docente}' NÃO foi encontrado.")
    
    cursor.close()

#ler notas
def ler_notas():
    conexao = criar_conexao() 
    cursor = conexao.cursor()
    

    cursor.execute("SELECT nome_aluno, notas_aluno FROM alunos")
    resultado = cursor.fetchall()
    
 
    dados_alunos = {i [0].lower(): i [1] for i in resultado}
    
 
    cursor.close()
    conexao.close()

    while True:
        print(dados_alunos)
        oq = input("De qual aluno você gostaria de ver as notas?\n: ").strip().lower()
        
      
        if oq in dados_alunos:
            print(f"Notas do aluno: {dados_alunos[oq]}")
            break
        else:
            print("Digite uma opção válida (Aluno não encontrado).")
            continue



#DEFs EXCLUIR


#excluir aluno
def excluir_aluno(matricula_ID):
    conexao = criar_conexao()  
    cursor = conexao.cursor()  
    
    sql = "DELETE FROM alunos WHERE matricula_ID = %s"
    cursor.execute(sql, (matricula_ID,)) 
    
    conexao.commit()  
    cursor.close()
    conexao.close()

#excluir professor
def excluir_professor(id_docente):
    conexao = criar_conexao()  
    cursor = conexao.cursor()  
    
    sql = "DELETE FROM professor WHERE id_docente = %s"
    cursor.execute(sql, (id_docente,)) 
    
    conexao.commit()  
    cursor.close()
    conexao.close()

#excluir nota
def excluir_nota(id_nota):
    cursor = criar_conexao()
    sql = "DELETE FROM notas WHERE id = %s"
    cursor.execute(sql, (id_nota,))
    cursor.commit()


#LISTAS


#Lista tendo todos as funcoes que um usuario pode ter no sistema
escolha_de_funcoes = ["professor", "coordenador", "diretor", "prof", "coord"]

#materias aceitas
materias_escola = ["biologia", "matematica","matemática", "geografia", "filosofia", "sociologia", "artes", "historia","história", "ingles", "edfisica", "edfísica", "fisica", "física", "portugues","português", "quimica", "coordenador", "diretor", "prof", "coord"]
