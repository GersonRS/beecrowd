while True:
    try:
        meses = {
            "1": 31,
            "2": 29,
            "3": 31,
            "4": 30,
            "5": 31,
            "6": 30,
            "7": 31,
            "8": 31,
            "9": 30,
            "10": 31,
            "11": 30,
            "12": 31,
        }

        mes, dia = map(int, input().split())

        if dia > 25 and mes == 12:
            print("Ja passou!")
        else:
            if mes == 12 and dia == 24:
                print("E vespera de natal!")
            elif mes == 12 and dia == 25:
                print("E natal!")
            else:
                dias_restantes = 366 - dia - 6
                soma_meses = 0
                for chave, valor in meses.items():
                    if int(chave) < mes:
                        soma_meses += valor
                dias_restantes -= soma_meses
                print(f"Faltam {dias_restantes} dias para o natal!")

    except:
        break
