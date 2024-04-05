# Завдання 3
# Запрограмуйте клас Money (об’єкт класу оперує однією
# валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої
# частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).
# Домашнє завдання
# 1
# Реалізуйте методи виведення суми на екран, задання
# значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для
# зменшення ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля.
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def display(self):
        print(f"${self.dollars}.{self.cents:02}")

    def decrease(self, amount):
        self.dollars -= amount.dollars
        self.cents -= amount.cents
        if self.cents < 0:
            self.dollars -= 1
            self.cents += 100

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name}, Price: ", end="")
        self.price.display()

    def reduce_price(self, reduction):
        self.price.decrease(reduction)


initial_price = Money(10, 50)  # Початкова ціна $10.50
product = Product("Laptop", initial_price)
product.display()

reduction = Money(3, 25)  # Знижка $3.25
product.reduce_price(reduction)
product.display()
