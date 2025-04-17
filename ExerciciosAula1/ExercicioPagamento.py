# Programa de Pagamento #

# Solicita os valores para o usuário
nome = input("Digite o nome do funcionário: ")
valor = float(input("Digite o valor p/ hora: R$"))
horas = float(input("Digite as horas trabalhadas: "))

# Calcula o valor do pagamento
pagamento = valor * horas

# Exibe mensagem explicativa correspondente ao seu salário
print(f"\n- Devido a quantidade de {horas} horas que o(a) funcionario(a) {nome} trabalhou, seu pagamento corresponde a: R${pagamento:.2f}")