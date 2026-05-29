# def ler_funcao(id_docente):
#     conn = criar_conexao()
#     cursor = conn.cursor()
#     sql = "SELECT * FROM professor WHERE id_docente = %s"

#     cursor.execute(sql, (id_docente,))

#     resultado = cursor.fetchone()

#     if resultado is None:
#         print("Docente não encontrado")
#         return

#     sql = "SELECT funcao_docente FROM professor WHERE id_docente = %s"
    
#     resultado = cursor.fetchone()

#     funcao_docente = resultado[0]


#     if resultado:
#         print(f"Seja bem vindo(a) {funcao_docente}")
#         match funcao_docente:
#             case "professor":
#                 return 1
#             case "coordenador":
#                 return 2
#             case "diretor":
#                 return 3

#     else:
#         print(f"O valor '{id_docente}' NÃO foi encontrado.")
    
#     cursor.close()
#     conn.close()