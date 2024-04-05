# Завдання 2
# Створіть клас Ship, який містить інформацію про кораблі.
# За допомогою механізму успадкування реалізуйте клас
# Frigate (містить інформацію про фрегат), клас Destroyer(містить
# інформацію про есмінця), клас Cruiser (містить інформацію
# про крейсер).
# Кожен із класів має містити необхідні для роботи методи
class Ship:
    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement

    def info(self):
        print(f"Name: {self.name}, Displacement: {self.displacement}")


class Frigate(Ship):
    def __init__(self, name, displacement, weapon_system):
        super().__init__(name, displacement)
        self.weapon_system = weapon_system

    def attack(self):
        print(f"{self.name} frigate attacks with {self.weapon_system}")


class Destroyer(Ship):
    def __init__(self, name, displacement, missile_system):
        super().__init__(name, displacement)
        self.missile_system = missile_system

    def launch_missile(self):
        print(f"{self.name} destroyer launches missile from {self.missile_system}")


class Cruiser(Ship):
    def __init__(self, name, displacement, radar_system):
        super().__init__(name, displacement)
        self.radar_system = radar_system

    def detect_enemy(self):
        print(f"{self.name} cruiser detects enemy using {self.radar_system}")
