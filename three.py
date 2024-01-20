class Monster:
    def __init__(self, health, power):
        self.__health = health
        self.__power = power

        if health < 1:
            self.__health = 1
        elif health > 100:
            self.__health = 100
        else:
            self.__health = health

        if power < 1:
            self.__power = 1
        elif power > 100:
            self.__power = 100
        else:
            self.__power = power

        if self.__power + self.__health < 2:
            self.__health = 1
            self.__power = 1
        elif self.__power + self.__health > 150:
            sr = self.__power + self.__health - 150
            if self.__health > self.__power:
                self.__health -= sr
            else:
                self.__power -= sr

        sum = self.__power + self.__health
        print(f"Суммарное значение здоровья и силы: {sum}")

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power


class1 = Monster(
    health=int(input("Введите здоровье: ")),
    power=int(input("Введите силу: "))
)
print("health: ", class1.get_health())
print("power: ", class1.get_power())