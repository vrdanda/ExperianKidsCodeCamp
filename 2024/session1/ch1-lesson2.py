# Conditional statements
# if, if else, if elif else
secret_code = 'Abracadabra'
entered_code = input('Enter the secret code: ')

if entered_code == secret_code:
    print('Door opens! Welcome inside!')

# Example - with if and else
entred_code = input('Enter the secret code: ')
if entered_code == secret_code:
    print('Door opens! Welcome inside!')
else:
    print('Bhoo, wrong code')

# Age example - with if, if elif and else
age = int(input('How old are you?'))
if age >= 10 and age <= 15:
    print('You are between 10 and 15 years old.')
elif age < 10:
    print('You are less than 10 years old.')
else:
    print("You're older than 15!")
