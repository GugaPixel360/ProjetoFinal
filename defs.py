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
            print("Sério? Ok né...")
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
        id_docente = input("Digite seu ID: ")

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

#adicionar alunos
def add_alunos():
    while True:

        conexao = criar_conexao()  
        cursor = conexao.cursor()

        nome = input("Digite o nome do aluno: ")
        print()
        idade = int(input("Digie a idade do aluno:"))
        print()
        print(turmas)
        turma = input("Digite a turma do aluno: ")

        if turma not in turmas:
            print("Turma não encontrada")
            continue

        cursor.execute(
            "INSERT INTO alunos (nome_aluno, idade_aluno, turma_aluno) VALUES (%s, %s, %s)",
            (nome, idade, turma)
        )

        conexao.close()
        cursor.close()
        break   

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

    return True

#adiciona nota ao aluno selecionado
def adicionar_nota(matricula):
    conn = criar_conexao()
    cursor = conn.cursor()

    while True:
        print ("Qual nota você gostaria de alterar?")
        resultado = ler_notas_notas(matricula)
        nota = input("Escreva aqui: ").strip().lower()

        if nota == "nota 1" or nota == "1":
            nota = "nota1"
            if resultado[1]:
                print("Essa nota já está adicionada, você gostaria de altera-la? \n | 1 - Sim \n | 2 - Não ")
                escolha = input("Escreva aqui: ")
                match escolha:
                    case "1":
                        try:
                            notaX = float(input("Digite a nova nota 1: "))
                        except:
                            erro()
                            print("Digite apenas números!")
                            continue
                    case "2":
                        return 
                    case _:
                        erro()
                        print("Escolha uma das opções dadas")
                        continue
            else:
                nota1 = float(input("Digite a nota 1: "))
        
        elif nota == "nota 2" or nota == "2":
            nota = "nota2"
            if resultado[2]:
                print("Essa nota já está adicionada, você gostaria de altera-la? \n | 1 - Sim \n | 2 - Não ")
                escolha = input("Escreva aqui: ")
                match escolha:
                    case "1":
                        try:
                            notaX = float(input("Digite a nova nota 2: "))
                        except:
                            erro()
                            print("Digite apenas números!")
                            continue
                    case "2":
                        return 
                    case _:
                        erro()
                        print("Escolha uma das opções dadas")
                        continue
            else:
                nota2 = float(input("Digite a nota 2: "))
        
        elif nota == "nota 3" or nota == "3":
            nota = "nota3"
            if resultado[3]:
                print("Essa nota já está adicionada, você gostaria de altera-la? \n | 1 - Sim \n | 2 - Não ")
                escolha = input("Escreva aqui: ")
                match escolha:
                    case "1":
                        try:
                            notaX = float(input("Digite a nova nota 2: "))
                        except:
                            erro()
                            print("Digite apenas números!")
                            continue
                    case "2":
                        return 
                    case _:
                        erro()
                        print("Escolha uma das opções dadas")
                        continue
            else:
                nota3 = float(input("Digite a nota 3: "))
        
        elif nota == "nota 4" or nota == "4":
            nota = "nota4"
            if resultado[4]:
                print("Essa nota já está adicionada, você gostaria de altera-la? \n | 1 - Sim \n | 2 - Não ")
                escolha = input("Escreva aqui: ")
                match escolha:
                    case "1":
                        try:
                            notaX = float(input("Digite a nova nota 4: "))
                        except:
                            erro()
                            print("Digite apenas números!")
                            continue
                    case "2":
                        return 
                    case _:
                        erro()
                        print("Escolha uma das opções dadas")
                        continue
            else:
                nota4 = float(input("Digite a nota 4: "))

        else:
            erro()
            print("Escolha uma das opções dadas")
            continue

        try:
            notaX = int(notaX)
        except:
            print("Sua nota precisa ser um número")
            erro()
            continue

        if notaX < 0 or notaX > 10:
            print("As notas precisam ser entre 0 e 10")
            erro()
            return

        sql = f"""
        INSERT INTO notas
            ({nota}, matricula_FK_ID)

        VALUES (%s, %s)
        """

        valores = (
            notaX,
            matricula
        )

        cursor.execute(sql, valores)
        ler_notas_notas(matricula)

        print("Você gostaria de adicionar mais notas?")
        print(" | 1 - Sim \n | 2 - não")
        op = input("Escreva aqui: ")
        match op:
            case "1":
                continue
            case "2":
                break 

        

    conn.commit()
    cursor.close()
    conn.close()



# atualizar nota do aluno
def atualizar_nota(matricula):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    while True:
        print("Qual nota você deseja atualizar?")
        print(" | 1 - Nota 1")
        print(" | 2 - Nota 2")
        print(" | 3 - Nota 3")
        print(" | 4 - Nota 4")

        opcao = input("Digite aqui: ").strip()

        notas = {
            "1": "nota1",
            "2": "nota2",
            "3": "nota3",
            "4": "nota4"
        }

        if opcao not in notas:
            erro()
            print("Escolha uma opção válida!")
            continue

        coluna = notas[opcao]

        try:
            nova_nota = float(input("Digite a nova nota: "))
        except:
            erro()
            print("Digite apenas números!")
            continue

        if nova_nota < 0 or nova_nota > 10:
            erro()
            print("A nota precisa estar entre 0 e 10")
            continue

        sql = f"""
        UPDATE notas
        SET {coluna} = %s
        WHERE matricula_FK_ID = %s
        """

        valores = (nova_nota, matricula)

        cursor.execute(sql, valores)
        conexao.commit()

        print("Nota atualizada com sucesso!")
        break

    cursor.close()
    conexao.close()




#adicionar professor (funcao diretor)
def adicionar_professor():

    
    while True:
        Nome = input("Digite o nome do professor: ").strip()

        if not validar_nome(Nome):
            print("Nome inválido!")
            erro()
            continue

        break

  
    while True:
        Email = input("Digite o email do professor: ").strip()

        if not validar_email(Email):
            continue

        break

    while True:
        materia = input("Digite a matéria do professor: ").strip().lower()

        if not validar_materia(materia):
            continue

        break

    senha = validar_senha()

    
    conexao = criar_conexao()

    cursor = conexao.cursor()

    try:
        sql = """
        INSERT INTO professor
        (nome_docente, email_docente, funcao_docente, materia_docente, senha)

        VALUES (%s, %s, %s, %s, %s)
        """

        valores = (
            Nome,
            Email,
        
            materia,
            senha
        )

        cursor.execute(sql, valores)
        conexao.commit()


    except Error as professor:
        print(f"Erro ao cadastrar professor: {professor}")
        erro()

        cursor.close()
        conexao.close()
    
#Cria a media de um aluno    
def media():
    while True:

        conn = criar_conexao()
        cursor = conn.cursor()

        id_aluno = int(input("Digite a matricula do aluno"))
        validar_matricula(id_aluno)

        if id_aluno.strip() == "":
            print("Campo vazio!")
            continue

        elif not id_aluno.isdigit():
            print("Apenas numeros!")
            continue

        
    
    


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

    cursor = conn.cursor()

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

    while True:
        print(dados_alunos)
        oq = input("De qual aluno você gostaria de ver as notas?\n: ").strip().lower()
        
      
        if oq in dados_alunos:
            print(f"Notas do aluno: {dados_alunos[oq]}")
            break
        else:
            print("Digite uma opção válida (Aluno não encontrado).")
            continue

#ler notas, apenas notas
def ler_notas_notas(matricula):
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
        print(f" | Aluno: {resultado[0]} \n | Nota 1: {resultado[1]}\n | Nota 2: {resultado[2]}\n | Nota 3: {resultado[3]}\n | Nota 4: {resultado[4]}")
    else:
        print("Aluno não encontrado.")

    return resultado

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
escolha_de_funcoes1 = ("Professor, Coordenador e diretor")

#materias aceitas
materias_escola = ["biologia","bio","mtm", "matematica","matemática","geo", "geografia","filo", "filosofia", "sociologia", "artes","hist", "historia","história", "ingles","ef", "edfisica", "edfísica", "fisica", "física", "portugues","português", "quimica", "coordenador", "diretor", "prof", "coord"]
materias_escola1 = ("Biologia, matemática, geografia, filosofia, sociologia, artes, história, inglês, educação física, Física, português, Química")

#array de turmas
turmas = ["001", "002", "003", "004", "005"]
