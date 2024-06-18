# Exception handling 
# Try Block: Think of this as your LEGO-building attempt. You put your code inside a “try” block. It’s like stacking bricks together.
# Excption Block: If something goes wrong (like a LEGO tower collapsing), the “except” block comes to the rescue. It catches the problem and tells you what went awry
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)
except:
    print("Oops! Denominator cannot be 0.")