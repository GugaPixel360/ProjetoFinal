from defs import *
from datetime import datetime


############################################################

# MENU PRINCIPAL!!!!!!!!!!!

############################################################


agora = datetime.now()

#Print inicial
print("======================================" )
print("Bem vindo ao menu da escola Carrossel!" )
print("======================================\n" )

print(f"|📅| Data: {agora.strftime('%d/%m/%Y')} ")
print(f"|⌚| Hora: {agora.strftime('%H:%M:%S')}\n")

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

                #coordendor
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
                funcao1 = verificar_funcao(funcao)


                if funcao1 != "coordenador" and funcao1 != "diretor":
                    #materia
                    materia = input(f"Digite a sua matéria \n | Matérias aceitas: {materias_escola1} \nDigite aqui: ").lower().strip()
                    if not validar_materia(materia):
                        erro()
                        continue
                    materia = validar_materia(materia)

                else:
                    materia = funcao1
                    
                #senha
                senha = validar_senha()

                print("\33[31m===============\033[m")  
                
                criar_login_professor(Nome, Email, funcao1, materia, senha)
                break 

            denovo()

        case _:
            erro()
            print("Escolha uma das opções dadas")
            continue
    

                