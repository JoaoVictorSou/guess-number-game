import random

secret_number = round(random.randrange(1,101))
tried = 3

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