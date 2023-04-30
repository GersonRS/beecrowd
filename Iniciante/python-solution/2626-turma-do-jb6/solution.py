while True:
    try:
        entrada = input().split()
        dodo = entrada[0]
        leo = entrada[1]
        pepper = entrada[2]

        if dodo == leo == pepper:
            print('Putz vei, o Leo ta demorando muito pra jogar...')
        elif dodo == 'papel':
            if leo == 'papel':
                if pepper == 'pedra':
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                else:
                    print('Urano perdeu algo muito precioso...')
            elif leo == 'tesoura':
                if pepper == 'tesoura':
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                elif pepper == 'papel':
                    print("Iron Maiden's gonna get you, no matter how far!")
                else:
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
            else:
                if pepper == 'papel':
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                elif pepper == 'tesoura':
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                else:
                    print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
        elif dodo == 'tesoura':
            if leo == 'papel':
                if pepper == 'pedra':
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                elif pepper == 'papel':
                    print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
                else:
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
            elif leo == 'tesoura':
                if pepper == 'tesoura':
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                elif pepper == 'papel':
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                else:
                    print('Urano perdeu algo muito precioso...')
            else:
                if pepper == 'papel':
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                elif pepper == 'tesoura':
                    print("Iron Maiden's gonna get you, no matter how far!")
                else:
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
        else:
            if leo == 'papel':
                if pepper == 'pedra':
                    print("Iron Maiden's gonna get you, no matter how far!")
                elif pepper == 'papel':
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                else:
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
            elif leo == 'tesoura':
                if pepper == 'tesoura':
                    print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
                elif pepper == 'papel':
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                else:
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
            else:
                if pepper == 'papel':
                    print('Urano perdeu algo muito precioso...')
                elif pepper == 'tesoura':
                    print('Putz vei, o Leo ta demorando muito pra jogar...')
                else:
                    print('Putz vei, o Leo ta demorando muito pra jogar...')

    except EOFError:
        break
