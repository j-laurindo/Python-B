def conversor():
    print("--- CONVERSOR DE TEMPERATURA ---")
    print("> Bem vindos, nesse programa você escolhe qual valor de temperatura você deseja converter e para qual unidade de medida, entre elas temos:")
    print("C = Celsius p/ Fahrenheit    |   F = Fahrenheit p/ Celsius")
    opcao = input("\n> Digite qual temperatura você deseja converter: ")

    if opcao == 'C' or opcao == 'c':
        print("\n-> Você escolheu C = Celsius p/ Fahrenheit")
        cel = float(input("> Digite a temperatura em Cº: "))
        fah = (cel * 1.8) + 32
        print(f"> Conversão de {cel:.1f}ºC para Fahrenheit: {fah:.1f}ºF\n\n-- Obrigado e volte sempre!")
    elif opcao == 'F' or opcao == 'f':
        print("\n-> Você escolheu F = Fahrenheit p/ Celsius")
        fah = float(input("> Digite a temperatura em Fº: "))
        cel = (5/9) * (fah - 32)
        print(f"> Conversão de {fah:.1f}ºF para Celsius: {cel:.1f}ºC \n\n-- Obrigado e volte sempre!")
    else:
        print("\n> OPÇÃO INVÁLIDA")

conversor()
