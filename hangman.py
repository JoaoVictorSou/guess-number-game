import random

def jogar():
    header()
    
    secret_word = secret_words_definer()
    win = False
    hanged = False
    err = 0
    right_word = ['_' for letter in secret_word]

    print(right_word)
    
    while (not win and not hanged):
        choose = handler_choose()
        
        if (choose in secret_word):
            letters_marker(choose, secret_word, right_word)
        else:
            err += 1
            draw(err)
        
        hanged = err == 7
        win = '_' not in right_word
        print(right_word)

    if (win):
        print_winner()
    elif (hanged):
        print_loser(secret_word)

    print('THE END')

def header():
    print('--------------- ****Py-gameStation**** ----------------')
    print('------------------------ FORCA ------------------------')
    print('----------------------- ******* -----------------------')

def secret_words_definer():
    words = []
    with open('palavras.txt', 'r') as file_words:
        for line in file_words:
            words.append(line.strip().upper())

    word_index = random.randrange(len(words))
    return words[word_index]

def handler_choose():
    choose = input('Qual letra? ')
    return choose.strip().upper()

def letters_marker(choose, secret_word, right_word):
    i = 0
    for letter in secret_word:
        if (choose.upper() == letter.upper()):
            right_word[i] = letter
                
        i += 1
    return right_word

def print_winner():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print('YOU WIN!')

def print_loser(secret_word):
    print('A PALAVRA ERA: {}'.format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print('GAME OVER!')

def draw(err):
    print("  _______     ")
    print(" |/      |    ")

    if(err == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif(err == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    elif(err == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif(err == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif(err == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif(err == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    elif (err == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == '__main__'):
    jogar()