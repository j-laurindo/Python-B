# Programa do Troco #

print("\n-- PAGAMENTO DE PRODUTO --\n")

# Define todas as inserções do usuário
preco = float(input("Digite o valor unitário do produto: R$"))
unidades = int(input("Digite a quantidade de unidades compradas: "))
pagamento = float(input("Digite o valor pago pelo cliente: R$"))

# Cálculos do valor e do troco
valor = preco * unidades
troco = pagamento - valor

# Exibição do resultado
print(f"\n-> VALOR DA COMPRA: R${valor:.2f}")
print(f"-> TROCO: R${troco:.2f}")