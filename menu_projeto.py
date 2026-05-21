from defs import *




############################################################

# MENU PRINCIPAL!!!!!!!!!!!

############################################################




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
            if not ler_docente():
                print("=================")
                print("Nenhum usuário encontrado.")
                print("=================")
                erro()
                continue

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
                    while True:
                        print("\33[30m==== OLÁ PROFESSOR DIGITE A OPÇÃO QUE VOCÊ DESEJA ALTERAR====\033[m")
                        op = input("0 - Sair \n | 1 - Nota \n | 2 - Situação do aluno \n | 3 - Informações do aluno \n").strip()

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
                                print("O que você gostaria de mexer?")
                                op = input("0 - Sair \n | 1 - adicionar \n | 2 - excluir").strip()
                                
                                if op.strip() == "":
                                    print("Campo vazio!")
                                    continue
                                    
                                match op:
                                    case "0":
                                        print("Você saiu")
                                        exit()

                                    case "1":
                                        matricula = input("Qual o aluno que você gostaria de adicionar nota (Escreva o numero da matricula): ")
                                        if not validar_matricula(matricula):
                                            print("Selecione uma das opcoes")
                                            erro()
                                            continue

                                        adicionar_nota(matricula)
                                            
                                    case "2":
                                        ler_notas()
                                        excluir_nota()
                                            
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

                            media(matricula)

                        #informacoes do aluno
                        elif op == "3":
                            ler_alunos_completo()
                            denovo()

                #coodenador
                case 2:
                    while True:
                        print("\33[30m==== OLÁ COORDENADOR DIGITE A OPÇÃO QUE VOCÊ DESEJA ALTERAR====\033[m")
                        op = input("0 - Sair \n | 1 - Nota \n | 2 - Situação do aluno \n | 3 - Informações do aluno \n | 4 - Alunos ").strip()

                        #Espaço vazio
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
                            print("O que você gostaria de mexer?")
                            op = input("0 - Sair \n | 1 - adicionar \n | 2 - excluir").strip()
                            
                            if op.strip() == "":
                                print("Campo vazio!")
                                continue
                                
                            match op:
                                case "0":
                                    print("Você saiu")
                                    break
                                
                                #adicionar
                                case "1":
                                    matricula = input("Qual o aluno que você gostaria de adicionar nota (Escreva o numero da matricula): ")
                                    if not validar_matricula(matricula):
                                        print("Selecione uma das opcoes")
                                        erro()
                                        continue

                                    adicionar_nota()
                                        
                                # excluir
                                case "2":
                                    ler_notas()
                                    excluir_nota()
                                        
                                # validacao
                                case _:
                                    erro()
                                    print("tente novamente")
                                    continue
                        
                        #situaçao do aluno
                        elif op == "2":
                            ler_alunos()
                            matricula = input("Qual aluno você gostaria de ver a média e a situação: ")
                            if not validar_matricula(matricula):
                                print("Selecione uma das opcoes")
                                erro()
                                continue

                            media(matricula)

                        elif op == "3":
                            ...
                        
                        #alunos, create e delete
                        elif op == "4":
                            ...        

                #diretor
                case 3:  
                    ...  

        case "2":

            while True:

                print ("\33[34m===============\033[m")
                
                #nome
                Nome = input("Digite seu nome completo: ").capitalize()               
                if not validar_nome(Nome):
                    erro()
                    print("Preencha o campo corretamente")
                    continue

                #email
                Email = input("Digite a seu email: ")
                if not validar_email(Email):
                    continue
                
                #funcao do docente
                funcao = input(f"Digite a sua função | funçoes: {escolha_de_funcoes1}\nEscreva aqui: ").lower().strip()
                if not verificar_funcao(funcao):
                    continue

                #materia
                materia = input(f"Digite a sua matéria (Caso nao seja professor repita a sua função)\n| Matérias aceitas: {materias_escola1} \nDigite aqui: ").lower().strip()
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
    

                



