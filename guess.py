secret_number = 43

choose = input('Digite o seu número: ')

print('Chute do usuário:', choose)

choose = int(choose)

if secret_number == choose:
    print('Acertou!')
elif (secret_number < choose):
    print('Faça chutes mais baixos!')
elif (secret_number > choose):
    print('Faça chutes mais altos!')
else:
    print('Caractere inválido!')
print('fim')