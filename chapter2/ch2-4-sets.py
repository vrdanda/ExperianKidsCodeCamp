# No Repeats:
# Sets don't allow duplicate items.

# Order Doesn’t Matter:
# The order of items in a set is irrelevant.

# Creating a Set:
favorite_colors = {"red", "blue", "green"}

# Add a new color to the set
favorite_colors.add("purple")

# Remove an existing color from the set
favorite_colors.remove("blue")

# Checking if Something’s in the Set:
if "blue" in favorite_colors:
    print("Blue is in my favorite colors!")

# Playing with Sets:
# Combine sets or find common elements.
set1 = {"Toyota", "Honda", "Ford", "BMW"}
set2 = {"Honda", "Tesla", "Ford", "Mercedes"}

# Combine the sets (union)
combined_set = set1 | set2

# Find common cars (intersection)
common_cars = set1 & set2

print("Combined set of cars:", combined_set)
print("Common cars:", common_cars)