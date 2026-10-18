class Device:
    def __init__(self, name, brand, power):
        self.name = name
        self.brand = brand
        self.power = power
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} увімкнено")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} вимкнено")

    def display(self):
        print(f"{self.name} ({self.brand}), {self.power} Вт")


class CoffeeMachine(Device):
    def __init__(self, name, brand, power, water_volume):
        super().__init__(name, brand, power)
        self.water_volume = water_volume

    def make_coffee(self):
        if self.is_on:
            print("Кава готова")
        else:
            print("Спочатку увімкніть кавомашину")


class Blender(Device):
    def __init__(self, name, brand, power, speeds):
        super().__init__(name, brand, power)
        self.speeds = speeds

    def blend(self, speed):
        if not self.is_on:
            print("Спочатку увімкніть блендер")
        elif speed > self.speeds:
            print(f"Максимальна швидкість: {self.speeds}")
        else:
            print(f"Змішую на швидкості {speed}")


class MeatGrinder(Device):
    def __init__(self, name, brand, power, capacity):
        super().__init__(name, brand, power)
        self.capacity = capacity

    def grind(self, kg):
        if self.is_on:
            minutes = kg / self.capacity
            print(f"Змолото {kg} кг м'яса за {minutes} хв")
        else:
            print("Спочатку увімкніть м'ясорубку")


coffee = CoffeeMachine("Кавомашина", "Philips", 1500, 1.8)
coffee.display()
coffee.make_coffee()
coffee.turn_on()
coffee.make_coffee()

print()
blender = Blender("Блендер", "Bosch", 800, 4)
blender.display()
blender.turn_on()
blender.blend(2)
blender.blend(6)

print()
grinder = MeatGrinder("М'ясорубка", "Moulinex", 1200, 2)
grinder.display()
grinder.grind(1.5)
grinder.turn_on()
grinder.grind(1.5)
grinder.turn_off()