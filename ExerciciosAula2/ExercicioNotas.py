# Entrada da Nota
print("--- CALCULO DE NOTA ANUAL ---\n")
nota1 = float(input("Digite a nota do primeiro semestre: "))
nota2 = float(input("Digite a nota do segundo semestre: "))

# Calculo da média final
final = (nota1 + nota2) / 2

# Lógica da nota final
if final >= 60.0:
    print(f"\n-> NOTA FINAL: {final:.1f}")
    print("-> Situação: O aluno foi APROVADO de ano")
else:
    print(f"\n-> NOTA FINAL: {final:.1f}")
    print("-> Situação: O aluno foi REPROVADO de ano")