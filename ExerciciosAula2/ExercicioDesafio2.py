senha_correta = "1234"
codigo_correto = 999
tentativa = 3

horario = input("Insira seu horário de acesso: ").replace(":","")
hora = int(horario[0:2])

if hora >= 8 and hora <= 18:
    usuario = input("Insira seu nome de usuário: ")
    if tentativa > 0:
        senha = input("Insira sua senha: ")
        if senha == senha_correta:

        else:
            tentativa =- 1
    elif tentativa == 1
    else:
        print("-> SISTEMA BLOQUEADO. Contate o administrador")


else:
    print("-> HORÁRIO DE ACESSO NÃO PERMITIDO! Tente novamente das 08 às 18 horas")
