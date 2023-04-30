horaI, minI, horaF, minF = map(int, input().split())

minI += horaI * 60
minF += horaF * 60

soma = minF-minI
if soma <= 0:
    soma += 24 * 60

hora = soma // 60
minutos = soma % 60

print(f'O JOGO DUROU {hora} HORA(S) E {minutos} MINUTO(S)')