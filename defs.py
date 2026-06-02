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
            print("=================\n")
            return

        elif continuar == "2":
            print("Você saiu, obrigado por ultilizar nosso sistema!")
            exit()
        else: 
            print("Valor inválido por favor responda com 1 ou 2.")
        print("=================")

#defs professor
def professor():
    while True:
        print("\33[30m==== OLÁ PROFESSOR DIGITE A OPÇÃO QUE VOCÊ DESEJA ALTERAR====\033[m")
        op = input(" | 0 - Sair \n | 1 - Nota \n | 2 - Média/Situação do aluno \n | 3 - Informações do aluno \n | Escreva aqui: ").strip()

        # espaço vazio
        if op.strip() == "":
            print("Campo vazio!")
            erro()
            continue

        # sair
        elif op == "0":
            print("Você saiu")
            exit()

        # manipular nota
        elif op == "1":
            while True:
                print("\nO que você gostaria de mexer?")
                op = input(" | 0 - Sair \n | 1 - Adicionar \n | 2 - Excluir\n | 3 - Vizualizar \n | Digite aqui: ").strip()
                                
                if op.strip() == "":
                    print("Campo vazio!")
                    continue
                                    
                match op:
                    case "0":
                        print("Você saiu")
                        exit()

                    # adicionar
                    case "1":
                        ler_alunos()
                        matricula = input("Qual o aluno que você gostaria de adicionar nota (Escreva o numero da matricula): ")
                        if not validar_matricula(matricula):
                            print("Selecione uma das opcoes")
                            erro()
                            continue

                        adicionar_nota(matricula)
                        if not denovo():
                            break

                    # excluir                                             
                    case "2":
                        ler_alunos()
                        matricula = input("Qual o aluno que você gostaria de excluir nota (Escreva o numero da matricula): ")
                        if not validar_matricula(matricula):
                            print("Selecione uma das opcoes")
                            erro()
                            continue
                        matricula = validar_matricula(matricula)
                        if not matricula:
                            erro()
                            continue

                        a, b = ler_notas_notas(matricula)

                        if not a:
                            continue

                        excluir_nota(matricula)
                        if not denovo():
                                            break
                                            
                    # ver notas 
                    case "3":
                        ler_alunos()
                        matricula = input("Qual o aluno que você gostaria de vizualizar as notas (Escreva o numero da matricula): ")
                        if not validar_matricula(matricula):
                            print("Selecione uma das opcoes")
                            erro()
                            continue
                        matricula = validar_matricula(matricula)
                        if not matricula:
                            erro()
                            continue

                        a, b = ler_notas_notas(matricula)

                        if not a:
                            continue

                        denovo()

                    case _:
                        erro()
                        print("tente novamente")
                        continue
        
        #situaçao do aluno
        elif op == "2":
            ler_alunos()
            matricula = input("Qual aluno você gostaria de ver a média e a situação: ")
            if not verificar_matricula(matricula):
                print("Selecione uma das opcoes")
                erro()
                continue

            if not validar_matricula(matricula):
                print("Selecione uma das opcoes")
                erro()
                continue

            media(matricula)

        #informacoes do aluno
        elif op == "3":
            ler_alunos_completo()
            if not denovo():
                break

        #validacao
        else:
            erro()
            print("Selecioe uma das opcoes")
            print("tente novamente")
            continue



# def coordenador 
def coordenador():
    while True:
        print("\33[30m==== OLÁ PROFESSOR DIGITE A OPÇÃO QUE VOCÊ DESEJA ALTERAR====\033[m")
        op = input(" | 0 - Sair \n | 1 - Nota \n | 2 - Média/Situação do aluno \n | 3 - Informações do aluno \n | 4 - Alunos \n | Escreva aqui: ").strip()

        # espaço vazio
        if op.strip() == "":
            print("Campo vazio!")
            erro()
            continue

        # sair
        elif op == "0":
            print("Você saiu")
            exit()

        # manipular nota
        elif op == "1":
            while True:
                print("\nO que você gostaria de mexer?")
                op = input(" | 0 - Sair \n | 1 - Adicionar \n | 2 - Excluir\n | 3 - Vizualizar \n | Digite aqui: ").strip()
                                
                if op.strip() == "":
                    print("Campo vazio!")
                    continue
                                    
                match op:
                    case "0":
                        print("Você saiu")
                        exit()

                    # adicionar
                    case "1":
                        ler_alunos()
                        matricula = input("Qual o aluno que você gostaria de adicionar nota (Escreva o numero da matricula): ")
                        if not validar_matricula(matricula):
                            print("Selecione uma das opcoes")
                            erro()
                            continue

                        adicionar_nota(matricula)
                        if not denovo():
                            break

                    # excluir                                             
                    case "2":
                        ler_alunos()
                        matricula = input("Qual o aluno que você gostaria de excluir nota (Escreva o numero da matricula): ")
                        if not validar_matricula(matricula):
                            print("Selecione uma das opcoes")
                            erro()
                            continue
                        matricula = validar_matricula(matricula)
                        if not matricula:
                            erro()
                            continue

                        a, b = ler_notas_notas(matricula)

                        if not a:
                            continue

                        excluir_nota(matricula)
                        if not denovo():
                                            break
                                            
                    # ver notas 
                    case "3":
                        ler_alunos()
                        matricula = input("Qual o aluno que você gostaria de vizualizar as notas (Escreva o numero da matricula): ")
                        if not validar_matricula(matricula):
                            print("Selecione uma das opcoes")
                            erro()
                            continue
                        matricula = validar_matricula(matricula)
                        if not matricula:
                            erro()
                            continue

                        a, b = ler_notas_notas(matricula)

                        if not a:
                            continue

                        denovo()

                    case _:
                        erro()
                        print("tente novamente")
                        continue
        
        #situaçao do aluno
        elif op == "2":
            ler_alunos()
            matricula = input("Qual aluno você gostaria de ver a média e a situação: ")
            if not verificar_matricula(matricula):
                print("Selecione uma das opcoes")
                erro()
                continue

            if not validar_matricula(matricula):
                print("Selecione uma das opcoes")
                erro()
                continue

            media(matricula)

        #informacoes do aluno
        elif op == "3":
            ler_alunos_completo()
            if not denovo():
                break

        #manipulaçao de alunos 
        elif op == "4":
            while True:
                print("\nO que você gostaria de mexer?")
                op = input(" | 0 - Sair \n | 1 - Adicionar \n | 2 - Excluir\n | 3 - Vizualizar \n | Digite aqui: ").strip()   

                if op.strip() == "":
                    print("Campo vazio!")
                    continue
                                    
                match op:
                    case "0":
                        print("Você saiu")
                        exit()

                    # adicionar
                    case "1":
                        ...
                        

                    # excluir                                             
                    case "2":
                        ler_alunos()
                        matricula = input("Qual o aluno que você gostaria de excluir (Escreva o numero da matricula): ")
                        if not validar_matricula(matricula):
                            print("Selecione uma das opcoes")
                            erro()
                            continue
                        matricula = validar_matricula(matricula)
                        if not matricula:
                            erro()
                            continue

                        a, b = ler_notas_notas(matricula)

                        if not a:
                            continue

                        excluir_nota(matricula)
                        if not denovo():
                                            break
                                            
                    # ver notas 
                    case "3":
                        ler_alunos()
                        matricula = input("Qual o aluno que você gostaria de vizualizar as notas (Escreva o numero da matricula): ")
                        if not validar_matricula(matricula):
                                            print("Selecione uma das opcoes")
                                            erro()
                                            continue
                        matricula = validar_matricula(matricula)
                        if not matricula:
                            erro()
                            continue

                        a, b = ler_notas_notas(matricula)

                        if not a:
                            continue

                        ler_notas_notas(matricula)
                        denovo()

                    case _:
                        erro()
                        print("tente novamente")
                        continue
        
        #validacao
        else:
            erro()
            print("Selecioe uma das opcoes")
            print("tente novamente")
            continue


# def diretor
def diretor():
    ...



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
        
        return
    
    return nota
    
#def validacao de materia
def validar_materia(materia):
    if materia.strip() == "":
        print("Campo vazio!")
        return False

    if materia not in materias_escola:
        print("Selecione uma matéria válida ou cargo")
        return False
    
    if materia == "prof":
        materia = "professor"
    if materia == "coord":
        materia = "coordenador"
    if materia == "bio":
        materia = "biologia"
    if materia == "mtm" or materia == "matematica":
        materia = "matemática"
    if materia == "geo":
        materia = "geografia"
    if materia == "filo":
        materia = "filosofia"
    if materia == "socio":
        materia = "sociologia"
    if materia == "hist" or materia == "historia":
        materia = "história"
    if materia == "ingles":
        materia = "inglês"
    if materia in eff:
        materia = "educação física"
    if materia == "fisica":
        materia = "física"
    if materia == "port" or materia == "port":
        materia = "português"
    if materia == "quimica":
        materia = "química"
    if materia == "coord":
        materia = "coordenador"
    if materia == "prof":
        materia = "professor"
        
    
    return materia

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
        conn = criar_conexao()
        cursor = conn.cursor()
        
        id_docente = input("Digite seu ID: ")

        if id_docente.strip() == "":
            print("Campo vazio!")
            continue

        if not id_docente.isdigit():
            print("Apenas números!")
            continue

        sql = "SELECT id_docente FROM professor WHERE id_docente = %s"

        cursor.execute(sql, (id_docente,))

        resultado = cursor.fetchone()

        if resultado is None:
            print("ID inválido!")
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
    
    if funcao == "prof":
        funcao = "professor"
    if funcao == "coor":
        funcao = "coordenador"
    
    return funcao

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

    try:
        matricula = int(matricula)
        return matricula
    except:
        erro()
        return 
    
#def validar matricula
def verificar_matricula(matricula):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    sql = "SELECT matricula_ID FROM alunos WHERE matricula_ID = %s"

    cursor.execute(sql, (matricula,))
    resultado = cursor.fetchall()

    if not resultado:
        print("Matricula não encontrada")
        
        cursor.close()
        conexao.close()
        return

    cursor.close()
    conexao.close()

    return True


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

        conexao.commit()
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
    resultado = cursor.fetchall()  
   
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
        print ("Qual nota você gostaria de adicionar?")
        a, resultado = ler_notas_notas(matricula)
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
                            continue

                        if not validar_nota(notaX):
                            erro()
                            continue
                        notaX = validar_nota(notaX)

                        atualizar_nota(matricula, notaX, nota)
                    case "2":
                        return 
                    case _:
                        erro()
                        print("Escolha uma das opções dadas")
                        continue
            else:
                notaX = float(input("Digite a nota 1: "))
        
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
                            continue

                        if not validar_nota(notaX):
                            erro()
                            continue
                        notaX = validar_nota(notaX)

                        atualizar_nota(matricula, notaX, nota)
                    case "2":
                        return 
                    case _:
                        erro()
                        print("Escolha uma das opções dadas")
                        continue
            else:
                notaX = float(input("Digite a nota 2: "))
        
        elif nota == "nota 3" or nota == "3":
            nota = "nota3"
            if resultado[3]:
                print("Essa nota já está adicionada, você gostaria de altera-la? \n | 1 - Sim \n | 2 - Não ")
                escolha = input("Escreva aqui: ")
                match escolha:
                    case "1":
                        try:
                            notaX = float(input("Digite a nova nota 3: "))
                        except:
                            erro()
                            continue

                        if not validar_nota(notaX):
                            erro()
                            continue
                        notaX = validar_nota(notaX)

                        atualizar_nota(matricula, notaX, nota)
                    case "2":
                        return 
                    case _:
                        erro()
                        print("Escolha uma das opções dadas")
                        continue
            else:
                notaX = float(input("Digite a nota 3: "))
        
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
                            continue

                        if not validar_nota(notaX):
                            erro()
                            continue
                        notaX = validar_nota(notaX)

                        atualizar_nota(matricula, notaX, nota)
                    case "2":
                        return 
                    case _:
                        erro()
                        print("Escolha uma das opções dadas")
                        continue
            else:
                notaX = float(input("Digite a nota 4: "))

        else:
            erro()
            print("Escolha uma das opções dadas")
            continue

        atualizar_nota(matricula, notaX, nota)
        ler_notas_notas(matricula)

        print("Você gostaria de adicionar mais notas?")
        print(" | 1 - Sim \n | 2 - não")
        op = input("Escreva aqui: ")
        match op:
            case "1":
                continue
            case "2":
                break 


    cursor.close()
    conn.close()

# atualizar nota do aluno
def atualizar_nota(matricula, notaX, nota):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    
    sql = f"""
        UPDATE notas
        SET {nota} = %s
        WHERE matricula_FK_ID = %s
        """

    valores = (notaX, matricula)
    cursor.execute(sql, valores)
    conexao.commit()

    print("---------------------------")
    print("Nota atualizada com sucesso!")
    print("---------------------------\n")

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
        "professor",
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
def media(matricula):
    while True:
        conn = criar_conexao()
        cursor = conn.cursor()

        sqlnome = "SELECT nome_aluno FROM alunos WHERE matricula_ID = %s"
        
        
        cursor.execute(sqlnome, (matricula,))

        resultnome = cursor.fetchall()[0][0]
        
        sql = "SELECT nota1, nota2, nota3, nota4 FROM notas WHERE matricula_FK_ID = %s"
        cursor.execute(sql, (matricula,))

        resultado = cursor.fetchone()

        cursor.close()
        conn.close()
        
        if any(item is None for item in resultado):
            print("Nem todas as notas foram adicionadas \nPor favor adicione todas as notas antes de gerar a média")
            return False
        
        if None in resultado:
            print("Nem todas as notas foram adicionadas.")
            print("Por favor adicione todas as notas antes de gerar a média.")
            return

        if resultado:
            nota1, nota2, nota3, nota4 = resultado    
            media = (nota1 + nota2 + nota3 + nota4) / 4
        
            print(f"Notas do {resultnome}: {nota1}, {nota2}, {nota3}, {nota4}")
            print(f"Média final: {media}")
        
        
            if media >= 7.0:
                print("Status: Aprovado")
            else:
                print("Status: Recuperação")
        else:
            print(f"Nenhuma nota encontrada para o aluno com ID {matricula}.")
        break


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
        print (f"Código do docente: {linha[0]} | Nome: {linha[1]} | Função: {linha[-1]}")

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

    if conn is None:
        return

    cursor = conn.cursor()

    sql = """
    SELECT funcao_docente
    FROM professor
    WHERE id_docente = %s
    """

    cursor.execute(sql, (id_docente,))

    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado is None:
        print("ID não encontrado")
        return

    funcao_docente = resultado[0]

    print(f"Seja bem vindo(a) {funcao_docente}")

    match funcao_docente:
        case "professor":
            return 1

        case "coordenador":
            return 2

        case "diretor":
            return 3

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


    cursor.close()
    conexao.close()
    return resultado

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

  

    if resultado is None:
        print("Aluno não encontrado.")
        return False, resultado

    print(f" | Aluno: {resultado[0]} \n | Nota 1: {resultado[1]}\n | Nota 2: {resultado[2]}\n | Nota 3: {resultado[3]}\n | Nota 4: {resultado[4]}")

    if resultado[1] is None and resultado[2] is None and resultado[3] is None and resultado[4] is None:
        print ("O aluno nao tem notas cadastradas")
        return False, resultado

    

    cursor.close()
    conexao.close()
    return True, resultado


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
def excluir_nota(matricula):
    conexao = criar_conexao()
    cursor = conexao.cursor()


    while True:
        nota = input("Qual nota você gostaria de excluir (Todas as notas - 5): ").strip()
        if nota == "5":
            excluir_5(matricula)

        ###############################################################

        if nota == "1" or nota == "nota 1":
            nota = "nota1"
            indice = 1

        elif nota == "2" or nota == "nota 2":
            nota = "nota2"
            indice = 2

        elif nota == "3" or nota == "nota 3":
            nota = "nota3"
            indice = 3

        elif nota == "4" or nota == "nota 4":
            nota = "nota4"
            indice = 4


        elif not nota in opcao_notas:
            print("Escolha uma das opções")
            continue

        a, b = ler_notas_notas(matricula)
        if b[indice] is None:
            print ("A nota escolhida não tem valor, não é possível exclui-la")

        elif True:
            sql = f"""
                UPDATE notas
                SET {nota} = NULL
                WHERE matricula_FK_ID = %s
                """
            
            valores = (matricula,)
            cursor.execute(sql, valores)
            conexao.commit()
        

        ler_notas_notas(matricula)
        cursor.close()
        conexao.close()

        #denovo
        print("Você gostaria de excluir mais notas?")
        print(" | 1 - Sim \n | 2 - não")
        op = input("Escreva aqui: ")
        match op:
            case "1":
                continue
            case "2":
                break 
    
#Excluir todas as notas
def excluir_5(matricula):
    conexao = criar_conexao() 
    cursor = conexao.cursor() 
    sql = """
    UPDATE notas
    SET nota1 = NULL,
        nota2 = NULL,
        nota3 = NULL,
        nota4 = NULL
    WHERE matricula_FK_ID = %s
    """

    valores = (matricula,)
    cursor.execute(sql, valores)
    conexao.commit()
            
    cursor.close()
    conexao.close()

    ler_notas_notas(matricula)
    



#LISTAS


#Lista tendo todos as funcoes que um usuario pode ter no sistema
escolha_de_funcoes = ["professor", "coordenador", "diretor", "prof", "coord"]
escolha_de_funcoes1 = ("Professor, Coordenador e diretor")

#educacao fisica
eff = ["edfisica", "edfísica","ef", "educaçao fisica", "educação fisica", "educaçao física", "educacao fisica", "educacão fisica", "educacao física"]

#materias aceitas
materias_escola = [ "biologia","bio","mtm", "matematica","matemática","geo", "geografia","filo", "filosofia","socio", "sociologia", "artes","hist", "historia","história", "ingles","inglês","ef", "edfisica", "edfísica", "fisica", "física","port", "portugues","português", "química", "quimica", "coordenador", "diretor", "prof", "coord"] + eff
materias_escola1 = ("Biologia, matemática, geografia, filosofia, sociologia, artes, história, inglês, educação física, Física, português, Química")

#array de turmas
turmas = ["001", "002", "003", "004", "005"]

#notas que existem no sql
opcao_notas = ["1", "nota 1", "nota1", "2", "nota 2", "nota2", "3", "nota 3", "nota3", "4", "nota 4", "nota4"]
