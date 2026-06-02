from defs import *




############################################################

# MENU PRINCIPAL!!!!!!!!!!!

############################################################




#Print inicial
print("======================================" )
print("Bem vindo ao menu da escola Carrossel!" )
print("======================================\n" )

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
                continue

            print("\33[31m===============\033[m")
            id_docente = validar_id() 
            senha = input("Digite a sua senha: ")   
            print("\33[31m===============\033[m") 

            if not Entrar(id_docente, senha):
                continue

            match ler_funcao(id_docente):

                #professor
                case 1:
                    professor()

                #coodenador
                case 2:
                    coordenador()
                                  
                #diretor
                case 3:  
                    diretor()

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
                funcao = input(f"Digite a sua função\n | funçoes: {escolha_de_funcoes1}\nEscreva aqui: ").lower().strip()
                if not verificar_funcao(funcao):
                    continue
                funcao = verificar_funcao(funcao)

                #materia
                materia = input(f"Digite a sua matéria (Caso nao seja professor repita a sua função)\n| Matérias aceitas: {materias_escola1} \nDigite aqui: ").lower().strip()
                if not validar_materia(materia):
                    erro()
                    continue
                materia = validar_materia(materia)
                
                #senha
                senha = validar_senha()
                print("\33[31m===============\033[m")  
                
                
                #criar login
                criar_login(Nome, Email, funcao, materia, senha)
                break
            denovo()

        case _:
            erro()
            print("Escolha uma das opções dadas")
            continue
    

                