secret_number = 43
tried = 3
round = 1

while (round <= tried):
    print('Rodada {} de {}'.format(round, tried))
    choose = input('Digite o seu número: ')
    print('Chute do usuário:', choose)
    choose = int(choose)

    if (secret_number == choose):
        print('Acertou!')
    elif (secret_number < choose):
        print('Faça chutes mais baixos!')
    elif (secret_number > choose):
        print('Faça chutes mais altos!')
    else:
        print('Caractere inválido!')
    round = round+1
print('fim')