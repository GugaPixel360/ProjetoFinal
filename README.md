#  Sistema Escolar Carrossel

## Descrição

O Sistema Escolar Carrossel é um sistema de gerenciamento escolar desenvolvido para controlar alunos, funcionários e notas, respeitando os diferentes níveis de acesso de cada usuário. O projeto foi desenvolvido utilizando os conceitos de Programação Orientada a Objetos (POO), aplicando boas práticas de organização e desenvolvimento de software.

---

## Objetivo

O objetivo do sistema é facilitar o gerenciamento das informações acadêmicas e administrativas de uma escola, permitindo que cada funcionário execute apenas as funções permitidas de acordo com seu cargo.

---

## Funcionalidades

### Alunos

- Cadastrar aluno.
- Visualizar alunos.
- Excluir aluno.

### Funcionários

- Cadastrar funcionário.
- Visualizar funcionários.
- Excluir funcionário.

### Notas

- Adicionar notas.
- Excluir notas.
- Visualizar notas.
- Calcular média do aluno.
- Exibir situação do aluno (Aprovado, Recuperação ou Reprovado).

---

## Controle de Acesso

### Professor

Pode:

- Visualizar alunos.
- Adicionar notas.
- Excluir notas.
- Visualizar notas.
- Calcular médias.
- Consultar situação dos alunos.

Não pode:

- Cadastrar ou excluir alunos.
- Cadastrar ou excluir funcionários.

### Coordenador

Possui todas as funções do professor e também pode:

- Cadastrar alunos.
- Excluir alunos.
- Visualizar alunos.
- Editar alunos

Não pode:

- Gerenciar funcionários.

### Diretor

Possui acesso completo ao sistema.

Pode:

- Gerenciar alunos.
- Gerenciar funcionários.
- Gerenciar notas.
- Visualizar todas as informações.

---

## Requisitos Funcionais

- Cadastro de alunos.
- Exclusão de alunos.
- Visualização de alunos.
- Cadastro de funcionários.
- Exclusão de funcionários.
- Visualização de funcionários.
- Cadastro de notas.
- Exclusão de notas.
- Visualização de notas.
- Cálculo automático da média.
- Exibição da situação do aluno.
- Controle de permissões conforme o cargo do funcionário.

---

## Requisitos Não Funcionais

- Login protegido por senha.
- Validação dos dados inseridos.
- Segurança das informações.
- Persistência de dados.
- Disponibilidade do sistema.
- Organização utilizando Programação Orientada a Objetos.

---

## Regras de Negócio

- Apenas usuários autenticados podem acessar o sistema.
- Professores podem manipular apenas informações acadêmicas.
- Coordenadores podem gerenciar alunos e notas.
- Diretores possuem acesso total.
- As notas devem estar dentro do intervalo permitido.
- A média é calculada automaticamente.
- A situação do aluno é determinada conforme sua média.

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/GugaPixel360/ProjetoFinal.git
```

2. Entre na pasta do projeto:

3. Compile o projeto:

4. Rode no terminal: "pip install mysql-connector-python" e "pip install pwinput" 

5. Execute 

---

## Melhorias Futuras

- Interface gráfica.
- Banco de dados MySQL ou PostgreSQL.
- Cadastro de disciplinas.
- Controle de frequência.
- Histórico escolar.
- Emissão de boletins.
- Cadastro de turmas.
- Recuperação de senha.
- Criptografia de senhas.

---

## Autores

- Josué
- Gabriel L.
- Gustavo

---
## Licença

Projeto desenvolvido para fins acadêmicos e educacionais.
