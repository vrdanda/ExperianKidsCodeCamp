def print_toys():
     print("Printing the favorite_toys list:")
     print(favorite_toys)
print_new_line = lambda: print()
    

# Collecting Toys:​
favorite_toys = ["teddy bear", "LEGO", "dinosaur"]
print_toys()
print_new_line()

# Adding and Removing Toys:​
 # Adding a new toy​
print("Adding race car as a new toy to favorite_toys list")
favorite_toys.append("race car") 
print_toys()
print_new_line()

# Removing a toy
favorite_toys.remove("LEGO")      
print("Removing LEGO")
print_toys()
print_new_line()

#Counting Toys:
print("Printing the length of the favorite toys list")
print(len(favorite_toys))  # Output: 3​
print_new_line()

# Finding a Specific Toy:​
print("Printing the second toy in the list which has index of 1: favorite_toys[1]")
print(favorite_toys[1])  # Output: "LEGO"​

