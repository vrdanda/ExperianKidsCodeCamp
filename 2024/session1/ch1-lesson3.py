def greet_wizard(name):
    return "Hello, " + name + "! May your potions always bubble."

# Example usage:​
wizard_name = "Merlin"
print(greet_wizard(wizard_name))

def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Example usage:
print(calculate_factorial(5))  
# Output: 120

import math
def find_square_root(number):
    return math.sqrt(number)
# Example usage:​
print(find_square_root(25))  # Output: 5.0

def sayHello(name):
    print("Hello Coach {}, Good afternoon".format(name))

# calling the function​
sayHello("Students")
