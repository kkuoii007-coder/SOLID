from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")

class Fighter:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"Боец выбрал новое оружие для боя")

    def attack(self, monster):
        self.weapon.attack()


class Monster:
    def __init__(self, name):
        self.name = name

    def die(self):
        print("Монстр побежден!")


monster = Monster("Гоблин")
fighter = Fighter("Винисиус", Sword())
fighter.attack(monster)
fighter.change_weapon(Bow())
fighter.attack(monster)
monster.die()