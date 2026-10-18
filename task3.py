class Money:
    def __init__(self, whole_part=0, cents=0, currency="грн"):
        self.currency = currency
        self.set_value(whole_part, cents)

    def set_value(self, whole_part, cents):
        total_cents = whole_part * 100 + cents
        if total_cents < 0:
            print("Сума не може бути від'ємною")
            total_cents = 0
        self.whole_part = total_cents // 100
        self.cents = total_cents % 100

    def display(self):
        print(f"{self.whole_part}.{self.cents:02d} {self.currency}")


class Product(Money):
    def __init__(self, name, whole_part, cents, currency="грн"):
        super().__init__(whole_part, cents, currency)
        self.name = name

    def reduce_price(self, discount_whole_part, discount_cents):
        price_in_cents = self.whole_part * 100 + self.cents
        discount_in_cents = discount_whole_part * 100 + discount_cents
        new_price_in_cents = price_in_cents - discount_in_cents

        if new_price_in_cents < 0:
            print("Знижка більша за ціну")
            return

        self.set_value(0, new_price_in_cents)

    def display(self):
        print(f"{self.name}:", end=" ")
        super().display()


money = Money()
money.set_value(10, 150)
money.display()

print()
bread = Product("Хліб", 35, 50)
bread.display()
bread.reduce_price(5, 75)
bread.display()
bread.reduce_price(100, 0)