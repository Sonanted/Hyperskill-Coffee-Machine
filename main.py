class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.action()

    def make_espresso(self):
        if self.water < 250:
            return 'Sorry, not enough water!\n'
        if self.milk < 0:
            return 'Sorry, not enough milk!\n'
        if self.coffee_beans < 16:
            return 'Sorry, not enough coffee beans!\n'
        if self.disposable_cups < 1:
            return 'Sorry, not enough disposable cups!\n'
        self.water -= 250
        self.milk -= 0
        self.coffee_beans -= 16
        self.disposable_cups -= 1
        self.money += 4
        return 'I have enough resources, making you a coffee!\n'

    def make_latte(self):
        if self.water < 350:
            return 'Sorry, not enough water!\n'
        if self.milk < 75:
            return 'Sorry, not enough milk!\n'
        if self.coffee_beans < 20:
            return 'Sorry, not enough coffee beans!\n'
        if self.disposable_cups < 1:
            return 'Sorry, not enough disposable cups!\n'
        self.water -= 350
        self.milk -= 75
        self.coffee_beans -= 20
        self.disposable_cups -= 1
        self.money += 7
        return 'I have enough resources, making you a coffee!\n'

    def make_cappuccino(self):
        if self.water < 200:
            return 'Sorry, not enough water!\n'
        if self.milk < 100:
            return 'Sorry, not enough milk!\n'
        if self.coffee_beans < 12:
            return 'Sorry, not enough coffee beans!\n'
        if self.disposable_cups < 1:
            return 'Sorry, not enough disposable cups!\n'
        self.water -= 200
        self.milk -= 100
        self.coffee_beans -= 12
        self.disposable_cups -= 1
        self.money += 6
        return 'I have enough resources, making you a coffee!\n'

    def action(self):
        act = input('Write action (buy, fill, take, remaining, exit):\n')
        while act != 'exit':
            if act == 'buy':
                self.buy()
            if act == 'fill':
                self.fill()
            if act == 'take':
                print(self.take())
            if act == 'remaining':
                self.remaining()
            act = input('Write action (buy, fill, take, remaining, exit):\n')

    def buy(self):
        coffee = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if coffee == '1':
            print(self.make_espresso())
        elif coffee == '2':
            print(self.make_latte())
        elif coffee == '3':
            print(self.make_cappuccino())

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:\n'))
        self.milk += int(input('Write how many ml of milk do you want to add:\n'))
        self.coffee_beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
        self.disposable_cups += int(input('Write how many disposable cups do you want to add:\n'))

    def take(self):
        dump = self.money
        self.money = 0
        return f'I gave you ${dump}\n'

    def remaining(self):
        print(f'''\nThe coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
{self.money} of money\n''')


cm = CoffeeMachine()
