# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

produto = float(input("Digite o preço do seu produto:"))
porcentagem = float(input("Digite a porcentagem de desconto: "))

desconto = produto*(porcentagem / 100)
valor_final= produto - desconto
print("Valor do desconto:", desconto)
print("Valor final do produto:", valor_final)                