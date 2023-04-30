while True:
    try:
        horario = {
            (0, 90): 'Bom Dia!!',
            (90, 180): 'Boa Tarde!!',
            (180, 270): 'Boa Noite!!',
            (270, 360): 'De Madrugada!!',
            (360, 361): 'Bom Dia!!',
        }

        x = int(input())
        for intervalo, mensagem in horario.items():
            if x in range(*intervalo):
                print(mensagem)

    except EOFError:
        break

