# MinMax.py

# Menu prompt.
print('\n************************************************************************************\
    \n\nWelcome to the Python MinMax Application!\n\nThis application calculates the minimum',
    'and maximum of 5 integer values entered by a user.\n\n')

# Prompts the user to enter 5 integers.
first = input('Enter your first integer:\n\n')

second = input('\nEnter your second integer:\n\n')

third = input('\nEnter your third integer:\n\n')

fourth = input('\nEnter your fourth integer:\n\n')

fifth = input('\nEnter your fifth integer:\n\n')

# Type casts String to int and finds the minimum and maximum values entered by the user.
print('\nThe minimum integer was' , min(int(first), int(second), int(third), int(fourth), int(fifth)),
    '\n\nThe maximum integer was' , max(int(first), int(second), int(third), int(fourth), int(fifth)))

# Exit prompt.
print('\nThanks for trying the Python MinMax Application!\
    \n\n*************************************************************************************\n')