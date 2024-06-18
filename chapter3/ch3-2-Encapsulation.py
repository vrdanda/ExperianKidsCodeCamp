# In this example, _battery_level is considered private and should only be used within the class itself.
# Keep in mind that Python doesn’t enforce strict privacy, but this naming convention helps indicate
# the intended visibility of class members.

class Toy:
    def __init__(self, name):
        self._name = name  # The toy's name (hidden inside the class)
        self._battery_level = 100  # Battery level (also hidden)

    def play(self):
        if self._battery_level > 0:
            print(f"{self._name} is playing!")
            self._battery_level -= 10
        else:
            print(f"{self._name} is out of battery. Recharge it!")

    def recharge(self):
        print(f"Charging {self._name}...")  # Recharge the battery
        self._battery_level = 100

# Let's create a toy car
car = Toy("SuperCar")

# Play with the car
car.play()  # Output: SuperCar is playing!
car.play()  # Output: SuperCar is playing!
car.play()  # Output: SuperCar is playing!

# Oops, it's out of battery
car.play()  # Output: SuperCar is out of battery. Recharge it!

# Recharge the car
car.recharge()  # Output: Charging SuperCar...
car.play()  # Output: SuperCar is playing!
