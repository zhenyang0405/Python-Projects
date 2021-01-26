def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('\nPlease, remind me your name.')
    name = input('Your name > ')
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('\nLet me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input('Remainder by 3 > '))
    rem5 = int(input('Remainder by 5 > '))
    rem7 = int(input('Remainder by 7 > '))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('\nNow I will prove to you that I can count to any number you want.')

    num = int(input('Please key in a number > '))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("\nLet's test your programming knowledge.")
    # write your code here
    print('''Why do we use methods?
1. To repeat a statement multiple times.
2. Ro decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.''')
    answer = None
    while answer != 2:
        answer = int(input('> '))
        if answer != 2:
            print('\nPlease, try again.')
            continue
        else:
            print('\nCompleted, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
