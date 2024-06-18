# Three Types of Tools in itertools:

# 1. Infinite Iterators:
# These are like never-ending roller coasters! They keep going forever.
# For example, you can create an infinite sequence of numbers: 1, 2, 3, 4, …
# It’s like counting to infinity without getting tired!

import itertools
import time

for i in itertools.count():
    print("Hello")
    time.sleep(10)

# 2. Terminating Iterators:
# These stop when they reach a certain point.
# Imagine you’re playing a game, and you collect coins until you have 10.
# The game stops when you reach your goal.
# Terminating iterators help us do similar things with data.

def count_to_20():
    count = 0
    for num in itertools.count(1):
        if count >= 20:
            break
        print(num)
        count += 1

count_to_20()

# 3. Combinatronic Iterators:
# These are like magic mixers for words and numbers.
# Let’s say you have colors (red, blue, green) and fruits (apple, banana, orange).
# Combinatronic iterators help you combine them in different ways:
# Red apple, blue banana, green orange!
# Blue apple, green banana, red orange!
# And so on!

def mix_color_and_fruit():
    colors = ['red', 'blue', 'green']
    fruits = ['apple', 'banana', 'orange']
    for color, fruit in itertools.product(colors, fruits):
        print(f"{color} {fruit}")

mix_color_and_fruit()
