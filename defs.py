import mysql.connector
from mysql.connector import Error


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
            print("Você saiu, obrigado por ultilizar nosso sistema!")
            exit()
        else:
            print("Valor inválido por favor responda com 1 ou 2.")
        print("=================")


#DEFs DE VALIDACAO!!!!



#validar nota
def validar_nota(nota):
    try:
        nota = float(nota)
    except:
        print("Digite uma nota válida!")
        return

    if nota > 10 or nota < 0:
        print("Sua nota precisa ser entra 0 e 10")
        erro()
        return
    
#def validacao de materia
def validar_materia(materia):
    if materia.strip() == "":
        print("Campo vazio!")
        return False

    if materia not in materias_escola:
        print("Selecione uma matéria válida ou cargo")
        return False

    return True

#def validar email
def validar_email(Email):
    if Email.strip() == "":
        erro()
        print("Campo vazio!")
        return False

    arroba = ["@gmail.com", "@hotmail.com", "@outlook.com", ]

    if not any(a in Email for a in arroba):
        print("Coloque o email corretamente")
        erro()
        return False

    return True

#defs validacao nome
def validar_nome(nome):
    nome.strip()

    if nome == "":
        print("Campo vazio!")
        return False
    if nome.replace(" ", "").isalpha():
        return True

    return False

# valida o id do docente que o usuario colocou 
def validar_id():
    while True:
        id_docente = input("Digite seu código do docente: ")

        if id_docente.strip() == "":
            print("Campo vazio!")
            continue

        if not id_docente.isdigit():
            print("Apenas números!")
            continue

        return id_docente

# verificacao da funcao do docente (se a funcao existe ou nao)
def verificar_funcao(funcao):
    funcao = funcao.lower()
    
    if not funcao in escolha_de_funcoes:
        erro()
        print("Escreva uma função existente!")
        print("----Funções: professor, coordenador, diretor----")

        return False
    
    return True

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

#def validacao de matricula
def validar_matricula(matricula):
    if matricula.strip() == "":
        print("Campo vazio!")
        return

    if not matricula.isdigit():
        print("A matrícula deve ter apenas números!")
        return
    
    return True

#def validar matricula
def verificar_matricula(matricula):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = "SELECT matricula_ID FROM alunos"

    cursor.execute(sql)

    resultado = cursor.fetchall()

    if matricula not in resultado:
        print("Matricula não encontrada")
        return
    
    cursor.close()
    conexao.close()


#DEFs DE LOGIN E CREATE                  


#def de cadastro
def criar_login(Nome, Email, funcao, materia, senha):
    conn = criar_conexao()

    if conn is None:
        print("Falha na conexão")
        return

    cursor = conn.cursor()

    if funcao == "prof":
        funcao = "professor"
    if funcao == "coord":
        funcao = "coordenador"

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

    return True

#adiciona nota ao aluno selecionado
def adicionar_nota(matricula):
    conn = criar_conexao()
    cursor = conn.cursor()
    while True:
        print ("Qual nota você gostaria de alterar?")
        ler_notas(matricula)
        escolha = input("Escreva aqui: ").strip().lower()

        
        match escolha:
            case "nota 1":
                if resultado[0]:
                    print("Essa nota já está adicionada, você gostaria de altera-la? \n | 1 - Sim \n | 2 - Não ")
                    escolha = input("Escreva aqui: ")
                    match escolha:
                        case "1":
                            nota1 = float(input("Digite a nota 1: "))
                        case "2":
                            return 
                        case _:
                            erro()
                            print("Escolha uma das opções dadas")
                            continue

                nota1 = float(input("Digite a nota 1: "))
                 












    try:
        nota2 = float(input("Digite a nota 2: "))
        nota3 = float(input("Digite a nota 3: "))
        nota4 = float(input("Digite a nota 4: "))

    except:
        print("Digite apenas números!")
        erro()
        return

    notas = [nota1, nota2, nota3, nota4]

    for nota in notas:
        if nota < 0 or nota > 10:
            print("As notas precisam ser entre 0 e 10")
            erro()
            return

    

    sql = """
    INSERT INTO notas
    (nota1, nota2, nota3, nota4, media_aluno, situacao_aluno, matricula_FK_ID)

    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        nota1,
        nota2,
        nota3,
        nota4,
        matricula
    )

    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

#Cria a media de um aluno    
def media(matricula):
    while True:

        conn = criar_conexao()
        cursor = conn.cursor()

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
    if not resultado:
        print("Nenhum usuário cadastrado")
        erro()
        return False
    

    # print docente    
    for linha in resultado:
        print (f"Código do docente: {linha[0]} | Nome: {linha[1]} | Função: {linha[2]}")

    cursor.close()
    conn.close()

    print ("=================")
    return True

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
    conn = criar_conexao()
    cursor = conn.cursor()

    if conn is None:
        print("Erro ao conectar com o banco!")
        return


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
    conn.close()

#retorna a funcao do docente
def ler_funcao(id_docente):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "SELECT funcao_docente FROM professor WHERE id_docente = %s"

    cursor.execute(sql, (id_docente,))

    resultado = cursor.fetchone()

    if resultado:
        funcao_docente = resultado[0]

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
    conn.close()

#ler notas
def ler_notas(matricula):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = """
    SELECT
        alunos.nome_aluno,
        notas.nota1,
        notas.nota2,
        notas.nota3,
        notas.nota4,
        notas.media_aluno,
        notas.situacao_aluno
    FROM alunos
    INNER JOIN notas
    ON alunos.matricula_ID = notas.matricula_FK_ID
    WHERE alunos.matricula_ID = %s
    """

    cursor.execute(sql, (matricula,))

    resultado = cursor.fetchone()

    if resultado:
        print(f"""
            Aluno: {resultado[0]}

            Nota 1: {resultado[1]}
            Nota 2: {resultado[2]}
            Nota 3: {resultado[3]}
            Nota 4: {resultado[4]}

            Média: {resultado[5]}
            Situação: {resultado[6]}
            """)
    else:
        print("Aluno não encontrado.")

    return resultado

    cursor.close()
    conexao.close()

   

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
escolha_de_funcoes1 = ("Professor, Coordenador e diretor")

#materias aceitas
materias_escola = ["biologia","bio","mtm", "matematica","matemática","geo", "geografia","filo", "filosofia", "sociologia", "artes","hist", "historia","história", "ingles","ef", "edfisica", "edfísica", "fisica", "física", "portugues","português", "quimica", "coordenador", "diretor", "prof", "coord"]
materias_escola1 = ("Biologia, matemática, geografia, filosofia, sociologia, artes, história, inglês, educação física, Física, português, Química")


