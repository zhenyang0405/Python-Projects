import random
import sqlite3


conn = sqlite3.connect('card.db')
cur = conn.cursor()

card_number = None
pin_number = None
user_input = int
checksum = 0
login = False

def run():
    global user_input
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')

    cur.execute("""CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL,
    pin TEXT NOT NULL,
    balance INTEGER DEFAULT 0
    );""")

    conn.commit()

    user_input = int(input())


def create_account():
    global card_number, pin_number, checksum
    bank_identifier = 400000
    acc_identifier = random.randint(99999999, 1000000000)
    checksum = random.randrange(0, 10)
    card_number = [str(bank_identifier), str(acc_identifier), str(checksum)]
    card_number = "".join(card_number)
    if luhn_algorithm(card_number) is True:
        print('Your card has been created')
        print('Your card number:')
        print(card_number)
        pin_number = random.randint(0, 9999)
        pin_number = str(pin_number).zfill(4)
        print('Your card PIN:')
        print(pin_number)
        cur.execute('INSERT INTO card (number, pin, balance) VALUES (?, ?, ?)', (card_number, pin_number, 0))
        conn.commit()
    else:
        create_account()


def luhn_algorithm(x):
    checked_card = list(x)
    checked_card.pop(-1)
    for i in range(0, len(checked_card)):
        checked_card[i] = int(checked_card[i])
    for i in range(0, len(checked_card), 2):
        checked_card[i] *= 2
    for i in range(0, len(checked_card)):
        if checked_card[i] > 9:
            checked_card[i] -= 9
    digits_sum = sum(checked_card) + int(checksum)
    if digits_sum % 10 == 0:
        return True


def log_in():
    global card_number, pin_number
    print('Enter your card number:')
    card_user_input = input()
    print('Enter your PIN:')
    pin_user_input = input()
    db_card = str(cur.execute('SELECT number FROM card').fetchall())
    db_pin = str(cur.execute(f'SELECT pin FROM card WHERE number = {card_user_input}').fetchall())
    if card_user_input in db_card:
        if pin_user_input in db_pin:
            card_number = card_user_input
            pin_number = pin_user_input
            print('You have successfully logged in!')
            return True
        else:
            print('Wrong card number or PIN!')
            return False
    else:
        print('Wrong card number or PIN!')
        return False


def balance():
    balance = cur.execute(f'SELECT balance FROM card WHERE number = {card_number}').fetchone()
    print(f'Account current balance: {str(balance[0])}')


def add_income():
    print('Enter income:')
    income = input()
    cur.execute('UPDATE card SET balance = balance + ? WHERE number = ?', (income, card_number))
    conn.commit()
    print('Income was added!')


def do_transfer():
    global checksum
    print('Transfer')
    print('Enter card number:')
    transfer_number = input()
    checksum = transfer_number[-1]
    if transfer_number == card_number:
        print('You can\'t transfer money to the same account!')
    elif luhn_algorithm(transfer_number) is True:
        all_account_number = cur.execute('SELECT number FROM card').fetchall()
        matched_account_number = [number for number in all_account_number if transfer_number in number]
        if transfer_number != matched_account_number[0][0]:
            print('Such a card does not exist.')
        else:
            print('Enter how much money you want to transfer:')
            transfer_money = int(input())
            balance_record = cur.execute(f'SELECT balance FROM card WHERE number = {card_number}').fetchone()
            if transfer_money <= balance_record[0]:
                cur.execute(f'UPDATE card SET balance = balance - {transfer_money} WHERE number = {card_number}')
                cur.execute(f'UPDATE card SET balance = balance + {transfer_money} WHERE number = {transfer_number}')
                conn.commit()
                print('Success!')
            else:
                print('Not enough money!')
    else:
        print('Probably you made mistake in the card number. Please try again!')


def close_account():
    cur.execute(f'DELETE FROM card WHERE number = {card_number}')
    conn.commit()
    print('The account has been closed!')


def logged():
    global login
    print('1. Balance')
    print('2. Add income')
    print('3. Do transfer')
    print('4. Close account')
    print('5. Log out')
    print('0. Exit')
    logged_user_input = int(input())
    if logged_user_input == 1:
        balance()
    elif logged_user_input == 2:
        add_income()
    elif logged_user_input == 3:
        do_transfer()
    elif logged_user_input == 4:
        close_account()
        login = False
    elif logged_user_input == 5:
        print('You have successfully logged out!')
        login = False
    elif logged_user_input == 0:
        exit()


while True:
    run()
    if user_input == 1:
        create_account()
    elif user_input == 2:
        login = log_in()
        while login == True:
            logged()
    elif user_input == 0:
        print('Bye!')
        conn.close()
        exit()