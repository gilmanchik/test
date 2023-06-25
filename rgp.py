# class Parent:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print(f'Hi my name is {self.name}')
#
#
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#     def greet(self):
#         super().greet()
#         print(f'My old {self.age} year')
#
#
# child = Child('Ivan', 5)
# child.greet()
import random



class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_target(self, target):
        damage = random.randint(1, self.attack)
        print(f'{self.name} hit {target.name} and makes {damage} damage')
        target.take_damage(damage)


class Player(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.portions = 3

    def use_portions(self):
        if self.portions > 0:
            self.health += 20
            self.portions -= 1
            print(f'{self.name} used portion and regeneration 20 points health')
        else:
            print("do not have portion")


class Enemy(Character):
    pass


def print_turn(func):
    def wrapper(*args, **kwargs):
        print('==== Start ====')
        res = func(*args, **kwargs)
        print('==== Edn ====')
        return res

    return wrapper


def random_damage(func):
    def wrapper(*args, **kwargs):
        damage = random.randint(1, 10)
        print(f'Damage: {damage}')
        kwargs['damage'] = damage
        return func(*args, **kwargs)

    return wrapper


def check_alive(func):
    def wrapper(*args, **kwargs):
        if args[0].is_alive():
            return func(*args, **kwargs)
        else:
            print('Character Died')

    return wrapper


def print_action(func):
    def wrapper(*args, **kwargs):
        action_name = func.__name__.replace('_', ' ').capitalize()
        print(f'{args[0].name} choice action: {action_name}')
        return func(*args, **kwargs)

    return wrapper


@print_action
@print_turn
@check_alive
@random_damage
def attack_target(attacker, target, damage):
    target.take_damage(damage)

@print_turn
@print_action
@check_alive
def use_portions(player):
    player.use_portions()

player = Player("Hero", 100, 20)
enemy = Enemy('Monster', 50, 10)

print("Welcome to the club body")

while player.is_alive() and enemy.is_alive():
    print(f'{player.name}: Health - {player.health},'
          f'health portions - {player.portions}')
    print(f'{enemy.name}: Health - {enemy.health}')

    choice = input('1 - Attack\n'
                   '2 - Used portions\n'
                   '(1-2): ')
    if choice == '1':
        attack_target(player, enemy)
        if not enemy.is_alive():
            print(f'{enemy.name} is Die')

    elif choice == '2':
        player.use_portions()
    else:
        print("Wrong choice")

    if enemy.is_alive():
        attack_target(enemy, player)
        enemy.attack_target(player)
        if not player.is_alive():
            print(f'{player.name} DIE')

print('End the game')
if player.is_alive():
    print('You win')
else:
    print('You lose')
