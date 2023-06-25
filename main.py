import time


class Device:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class CoffeeMachine(Device):
    water_volume = 0
    max_volume = 0.7
    max_water_volume = 1

    def get_type_coffee(self):
        type_coffee = input("Какой кофе? ")
        volume = float(input("Какой объем? "))
        if volume > self.max_volume:
            return f"Недопустимый объем"
        else:
            print('Готовим...')
            time.sleep(3)
            return f'Ваш кофе: {type_coffee}, объем: {volume}'

    def napolnenie(self, volume: int):
        if volume > self.max_water_volume:
            return f'Вы перелили'
        else:
            return self.water_volume + volume


coffeeMachine = CoffeeMachine("bosh", 23000)
print(coffeeMachine.napolnenie(5))
print(coffeeMachine.get_type_coffee())
