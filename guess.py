import random

secret_number = random.randrange(1,101)
tried = 0

level = int(input('Escolha o nível de dificuldade: 1 (fácil), 2 (médio) ou 3 (difícil): '))

if (level == 1):
    tried = 20
elif (level == 2):
    tried = 10
elif (level == 3):
    tried = 5
else:
    print('NÍVEL INVÁLIDO!')


for round in range(1, tried+1):
    print('Rodada {} de {}'.format(round, tried))
    choose = input('Digite um número entre 1 e 100: ')
    print('Chute do usuário:', choose)
    choose = int(choose)

    if (choose < 1 or choose > 100):
        print('Número fora do escopo')
        continue
    
    if (secret_number == choose):
        print('Acertou!')
        break
    elif (secret_number < choose):
        print('Faça chutes mais baixos!')
    elif (secret_number > choose):
        print('Faça chutes mais altos!')
    else:
         print('Caractere inválido!')
print('fim')