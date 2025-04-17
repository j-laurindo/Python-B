
print("--- CAIXA DA MERCEARIA ---\n")
preco = float(input("Digite o preço do produto: R$"))
quantidade = int(input("Digite a quantidade de produtos: "))
pagamento = float(input("Digite o valor pago pelo cliente: R$"))

valor = preco * quantidade

if pagamento >= valor:
    troco = pagamento - valor
    print(f"\n-> PREÇO TOTAL: R${valor:.2f}")
    print(f"-> PAGAMENTO: R${pagamento:.2f}")
    print(f"-> TROCO: R${troco:.2f}")
else:
    restante = valor - pagamento
    print("\n-- ALERTA: Não foi possível finalizar a compra, o valor total ainda não foi atingido")
    print(f"\n-> PREÇO TOTAL: R${valor:.2f}")
    print(f"-> PAGAMENTO: R${pagamento:.2f}")
    print(f"-> VALOR RESTANTE: R${restante:.2f}")

