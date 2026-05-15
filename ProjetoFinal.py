#Sistema escolar

#Requisitos: interface no terminal, sistema deve ter validaçâo de campos, o sistema  teve ter permanencia de dados, CRUD MINIMO: Criar dados, Visualizar dados, Atualizar
#e deletar dados, deve permitir cadastrar alunos, registrar notas, calclr medias, mostar situacao e manter dados salvos no MySQL
#Funcionalidades minimas: Cadastrar aluno, Listar alunos, Remover alunos, Editar dados dos alunos, Adicionar/remover notas, Buscar aluno

#SCRIPT SQL:

# CREATE DATABASE IF NOT EXISTS carrossel;

# USE carrossel;

# CREATE TABLE IF NOT EXISTS alunos (
# nome_aluno VARCHAR (100) NOT NULL,
# idade_aluno INT NOT NULL,
# turma_aluno INT NOT NULL,
# matricula_ID INT AUTO_INCREMENT PRIMARY KEY,
# notas_aluno INT
# );

# CREATE TABLE IF NOT EXISTS situacao (
# notas_aluno_FK INT,
# media_aluno INT,
# situacao_aluno VARCHAR (100),
# matricula_FK_ID INT AUTO_INCREMENT PRIMARY KEY,
# FOREIGN KEY (Matricula_FK_ID) REFERENCES Alunos (Matricula_ID)

# );

# CREATE TABLE IF NOT EXISTS professor (
# id_docente int auto_increment primary key,  
# nome_docente VARCHAR (100) NOT NULL,
# funcao_docente VARCHAR (50) NOT NULL,             
# email_docente VARCHAR (50) NOT NULL,
# senha VARCHAR (15) NOT NULL,
# materia_docente VARCHAR (100) NOT NULL
# );



import mysql.connector
from mysql.connector import Error

#Lista tendo todos as funcoes que um usuario pode ter no sistema
escolha_de_funcoes = ["professor", "coordenador", "diretor", "prof", "coord"]

#materias aceitas
materias_escola = ["biologia", "matematica","matemática", "geografia", "filosofia", "sociologia", "artes", "historia","história", "ingles", "edfisica", "edfísica", "fisica", "física", "portugues","português", "quimica", "coordenador", "diretor", "prof", "coord"]


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


#DEFs DE VALIDACAO!!!!


#def validacao de materia
def validar_materia(materia):
    if materia.strip() == "":
        print("Campo vazio!")
        return False

    if materia not in materias_escola:
        print("Selecione uma matéria válida")
        return False


#def validar email
def validar_email(email):
    if Email.strip() == "":
        erro()
        print("Campo vazio!")
        return False

#defs validacao nome
def validar_nome(Nome):
    if not Nome.isalpha():
        return False
    
    if Nome.strip() == "":
        erro()
        print("Campo vazio!")
        return False

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

# verificacao da funcao do docente (se a funcao existe ou nao)
def verificar_funcao(funcao):
    funcao = funcao.lower()
    
    if not funcao in escolha_de_funcoes:
        erro()
        print("Escreva uma função existente!")
        print("----Funções: professor, coordenador, diretor----")

        return False

# valida a senha na hora do create 
def validar_senha():
    while True:

        senha = input("Crie a sua senha: ")

        if senha.strip() == "":
            print("Campo vazio!")   


        letra = any(caracter.isalpha() for caracter in senha)
        num = any(caracter.isdigit() for caracter in senha)
        carac = any(not caracter.isalnum() for caracter in senha)
 
        if len(senha) > 10 or len(senha) < 1:
            print("Coloque menos de 10 valores")
            continue
           
        if letra and num and carac:
            print("Senha valida")
            return senha
            
            
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


#DEFs EXCLUIR


#excluir nota
def excluir_nota(id_nota):
    cursor = criar_conexao()
    sql = "DELETE FROM notas WHERE id = %s"
    cursor.execute(sql, (id_nota,))
    cursor.commit()



#Print inicial
print("Bem vindo ao menu da escola Carrossel!\n" )

while True:
    op = input("Você já tem login?\n | 0 - Sair \n | 1 - Entrar \n | 2 - Criar login\n | Escreva aqui: ").strip()

    if op.strip() == "":
        print("Campo vazio!")
        continue

    match op:
        case "0":
            print ("Você saiu")
            break
        
        case "1":
            ler_docente()

            print("\33[31m===============\033[m")
            id_docente = input("Digite seu ID: ")
            senha = input("Digite a sua senha: ")   
            print("\33[31m===============\033[m") 

            validar_id(id_docente) 
            if not Entrar(id_docente, senha):
                continue

            match ler_funcao(id_docente):

                #professor
                case 1:
                    print("\33[30m==== OLÁ PROFESSOR DIGITE A OPÇÃO QUE VOCÊ DESEJA ALTERAR====\033[m")
                    op = input("0 - Sair \n | 1 - Nota \n | 2 - Situação do aluno \n | 3 - Informações do aluno \n").strip()

                    if op.strip() == "":
                        print("Campo vazio!")
                        continue

                    elif op == "0":
                        print("Você saiu")
                        break

                    elif op == "1":
                            print("O que você gostaria de mexer?")
                            op = input("0 - Sair \n | 1 - adicionar \n | 2 - excluir").strip()

                            if op.strip() == "":
                                print("Campo vazio!")
                                continue
                            
                            match op:
                                case 0:
                                    print("Você saiu")
                                    break

                                case 1:
                                    adicionar_nota()


                                case 2:
                                    ler_notas()
                                    excluir_notas()

                                
                                case 3:
                                    ...
        
        case "2":
            while True:

                print ("\33[34m===============\033[m")
                
                #nome
                Nome = input("Digite seu nome completo: ").capitalize()               
                if not validar_nome():
                    erro()
                    print("Preencha o campo corretamente")
                    continue

                #email
                Email = input("Digite a seu email: ")
                if not validar_email(Email):
                    continue
                
                #funcao do docente
                funcao = input(f"Digite a sua função | funçoes: {escolha_de_funcoes}\n: ").lower()
                if not verificar_funcao(funcao):
                    continue

                #materia
                materia = input(f"Digite a sua matéria (Caso nao seja professor repita a sua função)\n| Matérias aceitas:\n {materias_escola} : ").lower()
                if not validar_materia(materia):
                    erro()
                    continue
                
                #senha
                senha = validar_senha()
                print("\33[31m===============\033[m")  
                
                
                #criar login
                criar_login(Nome, Email, funcao, materia, senha)
                denovo()

        case _:
            erro()
            print("Escolha uma das opções dadas")
            continue
    
        

                


            

