import random
import sys

programminglan_word_set = ['python', 'java', 'kotlin', 'javascript']
smartphonebrand_word_set = ['apple', 'samsung', 'huawei', 'oppo', 'oneplus']

count = 0
unique_word = set()

def word_set_option(set_option):
    if set_option == '1' or set_option == 'Programming Language':
        word_set = programminglan_word_set
    elif set_option == '2' or set_option == 'Smartphone Brand':
        word_set = smartphonebrand_word_set
    else:
        print('Invalid command!')
        exit()  

    random.seed()
    chosen_word = random.choice(word_set)
    return chosen_word

def play():
    global option
    global count

    print('Please choose a word set to start guessing.')
    set_option = input('''1 - Progamming Language
2 - Smartphone Brand\n''')

    chosen_word = word_set_option(set_option)
    hidden_word = ['-' for i in range(len(chosen_word))]
    print(''.join(hidden_word))

    while True:
        if count < 7:
            character = input('Input a letter: ')
            length_cha = len(character)
            if length_cha != 0 and length_cha == 1:
                if character.isalpha() == True and character.islower() == True:
                    if character not in unique_word:
                        unique_word.add(character)
                        if character in chosen_word:
                            for i, value in enumerate(chosen_word):
                                if value == character:
                                    hidden_word[i] = value
                        else:
                            print("No such letter in the word")
                            count += 1
                    else:
                        print('You already typed this letter')
                else:
                    print('It is not an ASCII lowercase letter')
            else:
                print('You should input a single letter')

            print()
            print(''.join(hidden_word))

        elif count == 7:
            character = input('Input a letter: ')
            length_cha = len(character)
            if length_cha != 0 and length_cha == 1:
                if character.isalpha() == True and character.islower() == True:
                    if character not in unique_word:
                        unique_word.add(character)
                        if character in chosen_word:
                            for i, value in enumerate(chosen_word):
                                if value == character:
                                    hidden_word[i] = value
                        else:
                            print("No such letter in the word")
                            print('You are hanged!\n')
                            break
                    else:
                        print('You already typed this letter')
                else:
                    print('It is not an ASCII lowercase letter')
            else:
                print('You should input a single letter')

            print()
            print(''.join(hidden_word))

        if '-' not in hidden_word:
            print(f'You guessed the word {chosen_word}!')
            print('You survived!\n')
            break

    option = input('Type "play" to play the game, "exit" to quit: ')

def exit():
    sys.exit()


print('H A N G M A N')
option = input('Type "play" to play the game, "exit" to quit: ')
print('')


if option == "play":
    play()
elif option == "quit":
    exit()
else:
    print("Invalid command!")