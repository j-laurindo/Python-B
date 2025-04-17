# Programa de Idades #

# Solicita o valor para os usuários
nome1 = input("Digite o nome da 1ª pessoa: ")
idade1 = int(input("Digite a idade da 1ª pessoa: "))
nome2 = input("Digite o nome da 2ª pessoa: ")
idade2 = int(input("Digite a idade da 2ª pessoa: "))

# Calcula a média da idade dos usuários
media = (idade1 + idade2) / 2

# Exibe uma mensagem com o nome, idade e idade média
print(f"\nPrimeira pessoa: \nNome: {nome1}  |  Idade: {idade1}\n")
print(f"Segunda pessoa: \nNome: {nome2}  |  Idade: {idade2}\n")
print(f"A idade média de {nome1} e {nome2} é igual a: {media:.1f}")
