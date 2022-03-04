import guess
import hangman

print('1 - Adivinhe o número\n2 - Forca')
game = int(input('O que desejas jogar: '))

if (game == 1):
    guess.jogar()
elif (game == 2):
    hangman.jogar()
else:
    print('OPÇÃO INVÁLIDA!')