# ############################################################

# # MENU PRINCIPAL!!!!!!!!!!!

# ############################################################




# #Print inicial
# print("Bem vindo ao menu da escola Carrossel!\n" )

# while True:
#     op = input("Você já tem login?\n | 0 - Sair \n | 1 - Entrar \n | 2 - Criar login\n | Escreva aqui: ").strip()

#     if op.strip() == "":
#         print("Campo vazio!")
#         continue

#     match op:
#         case "0":
#             print ("Você saiu")
#             break
        
#         case "1":
#             if not ler_docente():
#                 continue

#             print("\33[31m===============\033[m")
#             id_docente = validar_id() 
#             senha = input("Digite a sua senha: ")   
#             print("\33[31m===============\033[m") 

#             if not Entrar(id_docente, senha):
#                 continue

#             match ler_funcao(id_docente):

#                 #professor
#                 case 1:
#                     while True:
#                         print("\33[30m==== OLÁ PROFESSOR DIGITE A OPÇÃO QUE VOCÊ DESEJA ALTERAR====\033[m")
#                         op = input(" | 0 - Sair \n | 1 - Nota \n | 2 - Situação do aluno \n | 3 - Informações do aluno \n | Escreva aqui: ").strip()

#                         # espaço vazio
#                         if op.strip() == "":
#                             print("Campo vazio!")
#                             erro()
#                             continue

#                         # sair
#                         elif op == "0":
#                             print("Você saiu")
#                             exit()

#                         # manipular nota
#                         elif op == "1":
#                             while True:
#                                 print("\nO que você gostaria de mexer?")
#                                 op = input(" | 0 - Sair \n | 1 - adicionar \n | 2 - excluir\n | Digite aqui: ").strip()
                                
#                                 if op.strip() == "":
#                                     print("Campo vazio!")
#                                     continue
                                    
#                                 match op:
#                                     case "0":
#                                         print("Você saiu")
#                                         exit()

#                                     case "1":
#                                         ler_alunos()
#                                         matricula = input("Qual o aluno que você gostaria de adicionar nota (Escreva o numero da matricula): ")
#                                         if not validar_matricula(matricula):
#                                             print("Selecione uma das opcoes")
#                                             erro()
#                                             continue

#                                         adicionar_nota(matricula)
#                                         denovo()
                                            
#                                     case "2":
#                                         ler_notas()
#                                         excluir_nota()
                                            
#                                     case _:
#                                         erro()
#                                         print("tente novamente")
#                                         continue
        
#                         #situaçao do aluno
#                         elif op == "2":
#                             ler_alunos()
#                             matricula = input("Qual aluno você gostaria de ver a média e a situação: ")
#                             if not verificar_matricula(matricula):
#                                 print("Selecione uma das opcoes")
#                                 erro()
#                                 continue

#                             if not validar_matricula(matricula):
#                                 print("Selecione uma das opcoes")
#                                 erro()
#                                 continue

#                             media(matricula)



#                         #informacoes do aluno
#                         elif op == "3":
#                             ler_alunos_completo()
#                             denovo()

#                 #coodenador
#                 case 2:
#                     while True:
#                         print("\33[30m==== OLÁ COORDENADOR DIGITE A OPÇÃO QUE VOCÊ DESEJA ALTERAR====\033[m")
#                         op = input("0 - Sair \n | 1 - Nota \n | 2 - Situação do aluno \n | 3 - Informações do aluno \n | 4 - Alunos ").strip()

#                         #Espaço vazio
#                         if op.strip() == "":
#                             print("Campo vazio!")
#                             erro()
#                             continue

#                         # sair
#                         elif op == "0":
#                             print("Você saiu")
#                             exit()

#                         # manipular nota 
#                         elif op == "1":
#                             print("O que você gostaria de mexer?")
#                             op = input("0 - Sair \n | 1 - adicionar \n | 2 - excluir").strip()
                            
#                             if op.strip() == "":
#                                 print("Campo vazio!")
#                                 continue
                                
#                             match op:
#                                 case "0":
#                                     print("Você saiu")
#                                     break
                                
#                                 #adicionar
#                                 case "1":
#                                     ler_alunos()
#                                     matricula = input("Qual o aluno que você gostaria de adicionar nota (Escreva o numero da matricula): ")
#                                     if not validar_matricula(matricula):
#                                         print("Selecione uma das opcoes")
#                                         erro()
#                                         continue

#                                     adicionar_nota(matricula)
#                                     denovo()

                                                
#                                 # excluir
#                                 case "2":
#                                     ler_notas()
#                                     excluir_nota()
                                    
                                        
#                                 # validacao
#                                 case _:
#                                     erro()
#                                     print("tente novamente")
#                                     continue
                        
#                         #situaçao do aluno
#                         elif op == "2":
#                             ler_alunos()
#                             matricula = input("Qual aluno você gostaria de ver a média e a situação: ")
#                             if not verificar_matricula(matricula):
#                                 print("Selecione uma das opcoes")
#                                 erro()
#                                 continue

#                             if not validar_matricula(matricula):
#                                 print("Selecione uma das opcoes")
#                                 erro()
#                                 continue

#                             media(matricula)
                         
#                         elif op == "3":
#                             ler_alunos_completo()
#                             denovo()
                            
                        
#                         #alunos, create e delete
#                         elif op == "4":
#                             print("O que você gostaria de mexer?")
#                             op = input("0 - Sair \n | 1 - adicionar \n | 2 - excluir").strip()
                            
#                             if op.strip() == "":
#                                 print("Campo vazio!")
#                                 continue
                                
#                             match op:
#                                 case "0":
#                                     print("Você saiu")
#                                     break
                                
#                                 #adicionar
#                                 case "1":
#                                     add_alunos()
#                                     denovo()

                                                
#                                 # excluir
#                                 case "2":
#                                     ler_alunos()
#                                     excluir_aluno()
                                    
                                        
#                                 # validacao
#                                 case _:
#                                     erro()
#                                     print("tente novamente")
#                                     continue
                                  

#                 #diretor
#                 case 3:  
#                     ...  

#         case "2":

#             while True:

#                 print ("\33[34m===============\033[m")
                
#                 #nome
#                 Nome = input("Digite seu nome completo: ").capitalize()               
#                 if not validar_nome(Nome):
#                     erro()
#                     print("Preencha o campo corretamente")
#                     continue

#                 #email
#                 Email = input("Digite a seu email: ")
#                 if not validar_email(Email):
#                     continue
                
#                 #funcao do docente
#                 funcao = input(f"Digite a sua função\n | funçoes: {escolha_de_funcoes1}\nEscreva aqui: ").lower().strip()
#                 if not verificar_funcao(funcao):
#                     continue

#                 #materia
#                 materia = input(f"Digite a sua matéria (Caso nao seja professor repita a sua função)\n| Matérias aceitas: {materias_escola1} \nDigite aqui: ").lower().strip()
#                 if not validar_materia(materia):
#                     erro()
#                     continue
                
#                 #senha
#                 senha = validar_senha()
#                 print("\33[31m===============\033[m")  
                
                
#                 #criar login
#                 criar_login(Nome, Email, funcao, materia, senha)
#                 break
#             denovo()

#         case _:
#             erro()
#             print("Escolha uma das opções dadas")
#             continue
    

                

# Esse erro:

# 'NoneType' object has no attribute 'cursor'

# significa que alguma variável que deveria ser uma conexão com banco de dados está como None.

# Normalmente acontece em algo assim:

# conn = conectar()
# cursor = conn.cursor()

# mas conectar() falhou e retornou None.

# Como seu código principal usa:

# from defs import *

# o problema provavelmente está dentro do arquivo defs.py, em alguma função que conecta ao banco.

# Procure algo parecido com:

# def conectar():
#     try:
#         conn = sqlite3.connect("escola.db")
#         return conn
#     except:
#         print("Erro")

# ou MySQL:

# conn = mysql.connector.connect(...)

# e depois:

# cursor = conn.cursor()
# Como corrigir
# 1. Verifique a função de conexão

# Faça ela retornar corretamente a conexão:

# Exemplo SQLite
# import sqlite3

# def conectar():
#     try:
#         conn = sqlite3.connect("escola.db")
#         return conn
#     except Exception as erro:
#         print("Erro ao conectar:", erro)
#         return None
# 2. Antes de usar .cursor(), valide
# conn = conectar()

# if conn is None:
#     print("Falha na conexão")
#     return

# cursor = conn.cursor()
# O MAIS IMPORTANTE

# Você precisa descobrir QUAL função está causando isso.

# O erro completo normalmente mostra:

# File "...", line X
# cursor = conn.cursor()

# Manda esse traceback completo que eu consigo apontar exatamente a linha quebrada.

# Porque no código que você enviou não aparece nenhuma conexão com banco — então o erro está no defs.py.

# Achei o problema principal.
# O erro 'NoneType' object has no attribute 'cursor' acontece porque criar_conexao() às vezes retorna None, e você tenta usar .cursor() mesmo assim.

# Os pontos mais perigosos do seu código são estes:

# conn = criar_conexao()
# cursor = conn.cursor()

# Se a conexão falhar:

# conn = None

# então:

# conn.cursor()

# gera exatamente:

# 'NoneType' object has no attribute 'cursor'
# O ERRO MAIS PROVÁVEL

# Seu MySQL provavelmente NÃO está conectando.

# Então essa função:

# def criar_conexao():

# está entrando no:

# except Error as e:

# e retornando:

# return None
# COMO TESTAR

# Adicione isso logo depois da conexão:

# def criar_conexao():
#     try:
#         conexao = mysql.connector.connect(
#             host='127.0.0.1',
#             user='root',
#             password='Senac2026',
#             database='carrossel'
#         )

#         print("Conectado com sucesso!")  # <- ADD

#         return conexao

#     except Error as e:
#         print(f"Erro ao conectar: {e}")
#         return None
# POSSÍVEIS CAUSAS
# 1. MySQL desligado

# Abra o XAMPP/WAMP e ligue o MySQL.

# 2. Senha errada

# Você colocou:

# password='Senac2026'

# Talvez a senha do root seja diferente.

# Teste no Workbench.

# 3. Banco não existe

# Você usa:

# database='carrossel'

# Confirme se existe.

# No MySQL:

# SHOW DATABASES;
# 4. Porta errada

# Às vezes o MySQL usa outra porta.

# Tente:

# port=3306
# OUTROS ERROS NO SEU CÓDIGO

# Tem vários bugs além desse.

# 1. BUG GRAVE

# Em excluir_nota:

# cursor = criar_conexao()
# sql = "DELETE FROM notas WHERE id = %s"
# cursor.execute(sql, (id_nota,))
# cursor.commit()

# ERRADO.

# Você colocou a conexão dentro da variável cursor.

# Correto:

# def excluir_nota(id_nota):
#     conexao = criar_conexao()

#     if conexao is None:
#         return

#     cursor = conexao.cursor()

#     sql = "DELETE FROM notas WHERE id = %s"

#     cursor.execute(sql, (id_nota,))
#     conexao.commit()

#     cursor.close()
#     conexao.close()
# 2. BUG NO verificar_matricula

# Você usa:

# resultado = cursor.fetchall()

# if resultado is None:

# Mas fetchall() nunca retorna None.

# Retorna:

# []

# Correto:

# if not resultado:
# 3. BUG NO ler_notas_notas

# Aqui:

# linha = cursor.fetchall()
# resultado = linha[0]

# Se não existir nota:

# linha = []

# Então:

# linha[0]

# vai quebrar.

# Faça:

# linha = cursor.fetchall()

# if not linha:
#     print("Nenhuma nota encontrada")
#     return None

# resultado = linha[0]
# 4. BUG NO add_alunos

# Você esqueceu:

# conexao.commit()

# antes de fechar.

# 5. BUG NO SQL

# Aqui:

# sql = f"""
# INSERT INTO notas
#     ({notaX}, matricula_FK_ID)
# """

# notaX é valor da nota, não nome da coluna.

# Provavelmente você queria:

# sql = f"""
# INSERT INTO notas
#     ({nota}, matricula_FK_ID)
# VALUES (%s, %s)
# """
# 6. BUG NO UPDATE

# Aqui:

# SET {notaX} = %s

# notaX é número.

# Você queria:

# SET nota1 = %s

# ou:

# SET {nota} = %s
# 7. BUG NO validar_materia

# Você usa:

# if funcao == "prof":

# mas funcao não existe dentro da função.

# Vai dar:

# NameError
# RESUMO

# O erro principal é:

# conn = criar_conexao()
# cursor = conn.cursor()

# quando:

# criar_conexao() -> None

# Então:

# Verifique se MySQL está ligado
# Verifique senha
# Verifique banco carrossel
# Adicione:
# if conn is None:
#     return

# antes de qualquer .cursor().

# Seu sistema está ficando bom, mas precisa melhorar:

# tratamento de erros
# validação
# organização das queries
# commits
# fechamento de conexão

# Você já está fazendo bastante coisa avançada pra um CRUD escolar.

# linha = cursor.fetchall()

# if not linha:
#     print("Nenhuma nota encontrada")
#     return None

# resultado = linha[0]   porq retornar none

# O return None aí serve para indicar:

# “não encontrei nenhuma nota no banco”.

# Porque quando você faz:

# linha = cursor.fetchall()

# o MySQL retorna:

# uma lista com dados → se encontrou
# uma lista vazia [] → se NÃO encontrou

# Então:

# if not linha:

# significa:

# if linha == []:

# Exemplo:

# linha = []

# if not linha:
#     print("vazio")

# resultado:

# vazio
# Por que retornar None?

# Porque sem isso o código quebra aqui:

# resultado = linha[0]

# Se linha estiver vazia:

# linha = []

# então:

# linha[0]

# gera:

# IndexError: list index out of range

# Então você faz:

# if not linha:
#     print("Nenhuma nota encontrada")
#     return None

# para PARAR a função antes do erro.

# Exemplo completo
# def buscar():
#     linha = []

#     if not linha:
#         return None

#     resultado = linha[0]

#     return resultado
# O que acontece depois

# Quem chamar a função recebe None:

# resultado = buscar()

# print(resultado)

# saída:

# None
# Na prática

# Sua função:

# def ler_notas_notas(matricula):

# pode retornar:

# uma tupla com notas
# OU
# None

# Então depois você deve verificar:

# resultado = ler_notas_notas(matricula)

# if resultado is None:
#     return

# antes de usar:

# resultado[1]
# Melhor ainda: usar fetchone()

# Você só usa um resultado mesmo.

# Então pode simplificar:

# resultado = cursor.fetchone()

# if resultado is None:
#     print("Nenhuma nota encontrada")
#     return None

# Fica mais limpo e eficiente.

# se eu deixar so um return

# Sim. Em Python:

# return

# é a mesma coisa que:

# return None

# Exemplo:

# def teste():
#     return

# x = teste()

# print(x)

# saída:

# None

# Então você pode fazer:

# if not linha:
#     print("Nenhuma nota encontrada")
#     return

# e funciona igual.

# A diferença é só clareza:

# return → apenas sai da função
# return None → deixa explícito que não existe resultado

# Muitos programadores usam return None quando querem indicar:

# “a busca falhou” ou “não encontrei nada”.

# Mas os dois funcionam.