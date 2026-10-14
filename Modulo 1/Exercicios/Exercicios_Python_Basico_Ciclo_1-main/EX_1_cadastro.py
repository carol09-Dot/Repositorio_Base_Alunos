# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")
senha = int(input("Digite sua senha: "))


print("\n --- DADOS CADASTRADOS ---")
print("nome",nome)
print("idade",idade)
print("email",email)
print("senha",senha)