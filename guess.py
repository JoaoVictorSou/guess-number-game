import random

def jogar():
    secret_number = random.randrange(1,101)
    score = 500
    element = 0
    tried = 0

    print('------------------------ ADIVINHE O NÚMERO ------------------------')
    level = int(input('Escolha o nível de dificuldade: 1 (fácil), 2 (médio) ou 3 (difícil): '))

    if (level == 1):
        tried = 20
        element = 5
    elif (level == 2):
        tried = 10
        element = 10
    elif (level == 3):
        tried = 5
        element = 20
    else:
        print('NÍVEL INVÁLIDO!')


    for round in range(1, tried+1):
        print('Rodada {} de {}'.format(round, tried))
        choose = input('Digite um número entre 1 e 100: ')
        print('Chute do usuário:', choose)
        choose = int(choose)
        difference = abs(secret_number - choose)

        if (choose < 1 or choose > 100):
            print('Número fora do escopo')
            continue
        
        if (secret_number == choose):
            score += level * element + (tried - round)
            print('Acertou! YOU WIN!')
            print('Pontuação: {:.2f}'.format(score))
            break
        elif (tried == round):
            print('GAME OVER')
            print('Pontuação: {:.2f}'.format(score))
        elif (secret_number < choose):
            print('Faça chutes mais baixos!')
        elif (secret_number > choose):
            print('Faça chutes mais altos!')
        else:
            print('Caractere inválido!')
        score -= difference*element/4
    print('THE END')