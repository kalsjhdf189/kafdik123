class Monster:
    def __init__(self, health, power):
        self.__health = health
        self.__power = power

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self._health = health

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self._power = power

class1 = Monster(health = input("Введите здоровье: "), power = input("Введите силу: "))
print("health: ", class1.get_health())
print("power: ", class1.get_power())