# 
# String samples
#

# Changing Letters (Spelling Magic)​
# Let' say you want to change “cat” to “bat.” Python can do that!
# We use spells (called methods) to change letters:
word = "cat"
print(f'original word: {word}')  # Output: "bat"​
new_word = word.replace("c", "b")
print(f'new word: {new_word}')  # Output: "bat"​

# Mixing Words (String Concatenation)
# Imagine you have two magic scrolls: “Hello” and “world!” Python can combine them:​
greeting = "Hello"
ending = "world!"
full_message = greeting + " " + ending
print(full_message)  # Output: "Hello world!"​

# Counting Letters (Letter Spells)
# Python can count how many letters are in a word:
secret_code = "abracadabra"
num_letters = len(secret_code)
print("Number of letters:", num_letters)  # Output: 11​