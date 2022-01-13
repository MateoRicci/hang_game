import random
import os
import time

palabras_insertadas = []
letters = []
words = []
correct_letter = False
IMÁGENES_AHORCADO = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', '''
  +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']

def read():
    with open('./words.txt', 'r', encoding='UTF-8') as f:
        for word in f:
            words.append(word.rstrip('\n').lower())

def ocult(word):
    secret_word = str()
    for character in word:
        secret_word += '-'
        letters.append(character)
    return secret_word


def run():
    vidas = 0
    win = 0
    read()
    n = random.randint(0, len(words)-1)
    word = words[n]
    secret_word = ocult(word)
    change_secret_word = list(secret_word)

    print('\nBienvenido al juego del ahorcado!')
    
    while win == 0:
        no_fallo = 0
        fallo = False
        contador = 0
        check = False
        print('Tienes ', 6-vidas, ' vidas')
        print('\n',IMÁGENES_AHORCADO[vidas])
        print('\n', secret_word, '\n')
        if vidas > 0:
            print('Las palabras que has usado son: ', palabras_insertadas)

        letter = input('Ingrese una letra: ')
        try:
            letter = int(letter)
            print('\nERROR: Los numeros no son validos\n')
        except ValueError:
            if (len(letter) == 1) and (letter != ' '):
                for character in letters:
                    if letter.lower() == character:
                        change_secret_word[contador] = letter.lower()
                        secret_word = ''.join(change_secret_word)
                        no_fallo = 1
                        fallo = False
                    else:
                        fallo = True

                    contador += 1

                if (fallo == True) and (no_fallo == 0):
                    vidas += 1
                    palabras_insertadas.append(letter)                    

                for i in secret_word:
                    if i == '-':
                        check = False
                        break
                    else:
                        check = True

                if check == True:
                    win = 1

                if vidas == 6:
                    win = 2
                
            else:
                print('ERROR: Debes escribir 1 letra!')

        time.sleep(0.5)
        os.system('clear')

    if win == 1:
        print('\nHas ganado!! \n')
        print('La palabra era: ', word)
        print('\nTu puntaje fue: ', (6-vidas)**2, '\n')
    elif win == 2:
        print('\nHas perdido!\n')
        print('La palabra era: ', word, '\n')


if __name__ == '__main__':
    run()