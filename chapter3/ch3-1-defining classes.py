class Car:
    def __init__(self, color, brand):
        # This is a special method called the constructor; it's used when creating a new object
        self.color = color  # color and brand are two properties of the Car class
        self.brand = brand

    def drive(self):
        print(f"The {self.color} {self.brand} car is driving.")

    def honk(self):
        print(f"The {self.color} {self.brand} car is honking.")

# Example usage:
my_car = Car("red", "Toyota")
my_car.drive()

# ====================================================================================================

# Crayon class definition:
class Crayon:
    def __init__(self, color):
        self.color = color

    def draw(self):
        print(f"The {self.color} crayon is drawing.")

# Crayon class usage:
my_crayon = Crayon("blue")
my_crayon.draw()

# ====================================================================================================

# Teddy Bear class definition:
class TeddyBear:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def cuddle(self):
        print(f"The {self.color} teddy bear is cuddling.")

    def play(self):
        print(f"The {self.color} teddy bear is playing.")

# Teddy Bear class usage:
my_teddy_bear = TeddyBear("brown", "small")
my_teddy_bear.cuddle()