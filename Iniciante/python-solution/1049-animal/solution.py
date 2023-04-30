p1 = input()
p2 = input()
p3 = input()

dic = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba',
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca',
        },
    },
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta',
        },
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca',
        },
    },
}

try:
    print(dic[p1][p2][p3])
except KeyError:
    print("A combinação de inputs fornecidos não existe no dicionário.")