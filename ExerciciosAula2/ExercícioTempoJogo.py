## PARA FAZER: CORRIGIR O HORÁRIO MÍNIMO

inicial = input("Digite a hora inicial do jogo: ").replace(":","")
final = input("Digite a hora final do jogo: ").replace(":","")

# Convertendo string para int
hora_inicial = int(inicial[0:2])
minuto_inicial = int(inicial[2:5])

hora_final = int(final[0:2])
minuto_final = int(final[2:5])

# Condição - Hora Final no dia seguinte
if hora_final < hora_inicial:
    if minuto_final > minuto_inicial:                       # Condição Minuto - Verfica qual minuto é o maior para não imprimir ele negativo
        total_horas = (24 - hora_inicial) + hora_final      # Total Horas - Cálculo da hora, considerando a hora real e sua contagem de tempo
        print("esse é o total de horas: ",total_horas)
        total_minutos = minuto_final - minuto_inicial

        if total_horas <= 24 and total_horas >= 1:          # Condição 24HRS - Verifica se o total de horas ultrapassa as 24 horas
            print(f"A duração do jogo foi de {total_horas} hora(s) e {total_minutos} minuto(s)")
        else:
            print("-> A duração desse jogo ultrapassa o valor máximo de 24 horas")
    else:
        total_horas = (24 - hora_inicial) + hora_final
        total_minutos = minuto_inicial - minuto_final

        if total_horas <= 24:
            print(f"A duração do jogo foi de {total_horas} hora(s) e {total_minutos} minuto(s)")
        else:
            print("-> A duração desse jogo ultrapassa o valor máximo de 24 horas")

# Condição - Hora Final no mesmo dia
elif hora_final > hora_inicial:
    if minuto_final > minuto_inicial:                       # Condição Minuto - Verfica qual minuto é o maior para não imprimir ele negativo
        total_horas = hora_final - hora_inicial
        total_minutos = minuto_final - minuto_inicial

        if total_horas <= 24:                               # Condição 24HRS - Verifica se o total de horas ultrapassa as 24 horas
            print(f"-> A duração do jogo foi de {total_horas} hora(s) e {total_minutos} minuto(s)")
        else:
            print("-> A duração desse jogo ultrapassa o valor máximo de 24 horas")
    else:
        total_horas = hora_final - hora_inicial
        total_minutos = minuto_inicial - minuto_final

        if total_horas <= 24:
            print(f"-> A duração do jogo foi de {total_horas} hora(s) e {total_minutos} minuto(s)")
        else:
            print("-> A duração desse jogo ultrapassa o valor máximo de 24 horas")

