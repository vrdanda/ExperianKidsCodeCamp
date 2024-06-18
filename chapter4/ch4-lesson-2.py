# Types of Exceptions:
# https://www.w3schools.com/python/python_ref_exceptions.asp
# Examples: ZeroDivisionError, IndexError
#

# Example-1 that throws IndexError excption.
try:
    even_numbers = [2, 4, 6, 8]
    print('Second elemnent from the evens list:' + str(even_numbers[1])) # Prints 2nd element.
    print(even_numbers[5])  # Oops! Index 5 doesn't exist!​
except ZeroDivisionError:
    print("Oops! Denominator cannot be 0.")
except IndexError:
    print("Oops! Index out of bounds.")

#
# Example-2
#
try:
    num = input("Enter a number: ")
    assert num.isnumeric()
    reciprocal = 1 / int(num)
except AssertionError:
    print("Assertion error - Not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"The reciprocal is {reciprocal:.2f}")