class Ship:
    def __init__(self, name, length, crew, speed):
        self.name = name
        self.length = length
        self.crew = crew
        self.speed = speed

    def display(self):
        print(f"{self.name}: довжина {self.length} м, екіпаж {self.crew}, швидкість {self.speed} вузлів")

    def sail(self, distance):
        hours = distance / self.speed
        print(f"{self.name} пройде {distance} миль за {hours} год")


class Frigate(Ship):
    def __init__(self, name, length, crew, speed, helicopters):
        super().__init__(name, length, crew, speed)
        self.helicopters = helicopters

    def patrol(self):
        print(f"{self.name} патрулює з {self.helicopters} вертольотами")


class Destroyer(Ship):
    def __init__(self, name, length, crew, speed, torpedoes):
        super().__init__(name, length, crew, speed)
        self.torpedoes = torpedoes

    def fire_torpedo(self):
        if self.torpedoes > 0:
            self.torpedoes = self.torpedoes - 1
            print(f"Торпеду випущено. Залишилось: {self.torpedoes}")
        else:
            print("Торпеди закінчились")


class Cruiser(Ship):
    def __init__(self, name, length, crew, speed, missiles):
        super().__init__(name, length, crew, speed)
        self.missiles = missiles

    def launch_missiles(self, count):
        if count > self.missiles:
            print(f"Недостатньо ракет. Є лише {self.missiles}")
        else:
            self.missiles = self.missiles - count
            print(f"Запущено {count} ракет. Залишилось: {self.missiles}")


frigate = Frigate("Фрегат Гетьман", 120, 200, 30, 2)
frigate.display()
frigate.sail(60)
frigate.patrol()

print()
destroyer = Destroyer("Есмінець Сокіл", 150, 300, 35, 2)
destroyer.display()
destroyer.fire_torpedo()
destroyer.fire_torpedo()
destroyer.fire_torpedo()

print()
cruiser = Cruiser("Крейсер Україна", 180, 500, 25, 10)
cruiser.display()
cruiser.launch_missiles(4)
cruiser.launch_missiles(8)