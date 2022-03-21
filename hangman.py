def jogar():
    print('------------------------ FORCA ------------------------')
    
    secret_word = 'banana'.upper()
    win = False
    hanged = False
    err = 0
    right_word = ['_' for letter in secret_word]

    print(right_word)
    
    while (not win and not hanged):
        choose = input('Qual letra? ')
        choose = choose.strip().upper()

        i = 0
        
        if (choose in secret_word):
            for letter in secret_word:
                if (choose.upper() == letter.upper()):
                    right_word[i] = letter
                
                i += 1
        
        else:
            err += 1
        
        hanged = err == 6
        win = '_' not in right_word
        print(right_word)

    if (win):
        print('YOU WIN!')
    elif (hanged):
        print('GAME OVER!')
    print('THE END')

if (__name__ == '__main__'):
    jogar()