# For Loop:
# Use it to iterate over a sequence (e.g., a list) and perform an action for each item.
candies = ["Chocolate", "Gummy Bears", "Lollipops"]
for candy in candies:
    print("Yum!", candy)

# While Loop:
# Use it to keep doing something until a condition is met (e.g., playing hide-and-seek).
count = 1
while count <= 10:
    print("Counting:", count)
    count += 1

# Break and Continue:
# - Use 'break' to stop the loop early (like finding a treasure during a hunt).
# - Use 'continue' to skip one step and continue to the next.
for number in range(1, 11):
    if number == 5:
        break  # Stop when we find 5
    print("Number:", number)