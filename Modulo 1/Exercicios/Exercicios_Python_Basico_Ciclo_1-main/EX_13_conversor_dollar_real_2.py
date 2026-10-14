# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


print("""
Escolha uma opção
1 - Dolar para real
2- Real para dolar        
      """)

cot = float(input("Informe a cotação atual do dólar: ")) 

opcao = int(input("Digite uma opção: "))
if opcao == 1:
    dol = float(input("Informe a quantidade de dólares: "))
    print(f"o valor em reais é R${dol*cot:.2f}")

elif opcao == 2:
    reais = float(input("Informe a quantidade de reais: "))
    print(f"o valor em dólares é US$ {reais/cot:.2f}")

else:
    print("Opção inválida!")