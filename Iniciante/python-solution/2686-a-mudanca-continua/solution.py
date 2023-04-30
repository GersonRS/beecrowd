while True:
    try:
        entrada = input().strip()
        if not entrada:
            break

        grau = float(entrada) % 360

        if grau < 90:
            print("Bom Dia!!")
        elif grau < 180:
            print("Boa Tarde!!")
        elif grau < 270:
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")

        grau_em_minutos = grau * 4
        horas = int(grau_em_minutos // 60) + 6
        minutos = int(grau_em_minutos % 60)
        segundos = round((grau_em_minutos - int(grau_em_minutos)) * 60)
        if horas >= 24:
            horas -= 24
        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

    except EOFError:
        break
