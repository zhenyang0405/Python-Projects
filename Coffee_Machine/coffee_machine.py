import sys

class CoffeeMachine:

    def __init__(self, has_water, has_milk, has_coffee_beans, has_cups, has_money):
        self.has_water = has_water
        self.has_milk = has_milk
        self.has_coffee_beans = has_coffee_beans
        self.has_cups = has_cups
        self.has_money = has_money

    def menu(self):
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()
        if action != 'exit':
            if action == 'buy':
                CoffeeMachine.buy(self)
            elif action == 'fill':
                CoffeeMachine.fill(self)
            elif action == 'take':
                CoffeeMachine.take(self)
            elif action == 'remaining':
                CoffeeMachine.remaining(self)
            else:
                print('Invalid command!')
        else:
            CoffeeMachine.exit(self)

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        choice = input()
        if choice == '1':
            if self.has_water >= 250 and self.has_coffee_beans >= 16 and self.has_cups >= 1:
                self.has_water -= 250
                self.has_coffee_beans -= 16
                self.has_cups -= 1
                self.has_money += 4
                print('I have enough resources, making you a coffee!')
            else:
                if self.has_water < 250:
                    print('Sorry, not enough water!')
                if self.has_coffee_beans < 16:
                    print('Sorry, not enough coffee beans!')
                if self.has_cups < 1:
                    print('Sorry, not enough disposable cups!')
        elif choice == '2':
            if self.has_water >= 350 and self.has_milk >= 75 and self.has_coffee_beans >= 20 and self.has_cups >= 1:
                self.has_water -= 350
                self.has_milk -= 75
                self.has_coffee_beans -= 20
                self.has_cups -= 1
                self.has_money += 7
                print('I have enough resources, making you a coffee!')
            else:
                if self.has_water < 350:
                    print('Sorry, not enough water!')
                if self.has_milk < 75:
                    print('Sorry, not enough milk!')
                if self.has_coffee_beans < 20:
                    print('Sorry, not enough coffee beans!')
                if self.has_cups < 1:
                    print('Sorry, not enough disposable cups!')
        elif choice == '3':
            if self.has_water >= 200 and self.has_milk >= 100 and self.has_coffee_beans >= 12 and self.has_cups >= 1:
                self.has_water -= 200
                self.has_milk -= 100
                self.has_coffee_beans -= 12
                self.has_cups -= 1
                self.has_money += 6
                print('I have enough resources, making you a coffee!')
            else:
                if self.has_water < 200:
                    print('Sorry, not enough water!')
                if self.has_milk < 100:
                    print('Sorry, not enough milk!')
                if self.has_coffee_beans < 12:
                    print('Sorry, not enough coffee beans!')
                if self.has_cups < 1:
                    print('Sorry, not enough disposable cups!')
        else:
            CoffeeMachine.menu(self)
        return self.has_water, self.has_milk, self.has_coffee_beans, self.has_cups, self.has_money

    def remaining(self):
        print('The coffee machine has:')
        print(f'{str(self.has_water)} of water')
        print(f'{str(self.has_milk)} of milk')
        print(f'{str(self.has_coffee_beans)} of coffee beans')
        print(f'{str(self.has_cups)} of disposable cups')
        print(f'${str(self.has_money)} of money')

    def fill(self):
        print('Write how many ml of water do you want to add:')
        water = int(input())
        print('Write how many ml of milk do you want to add:')
        milk = int(input())
        print('Write how many grams of coffee beans do you want to add:')
        coffee = int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        cups = int(input())

        self.has_water += water
        self.has_milk += milk
        self.has_coffee_beans += coffee
        self.has_cups += cups

        return self.has_water, self.has_milk, self.has_coffee_beans, self.has_cups

    def take(self):
        print(f'I give you ${self.has_money}')

        self.has_money = 0
        return self.has_money

    def exit(self):
        sys.exit()

coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    coffee_machine.menu()