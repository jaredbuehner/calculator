# Calculator.py

# Menu prompt.
print('\n************************************************************************************\
    \n\nWelcome to the Python Calculator Application!\n\nWhat calculation do you want to perform?',
    '\n\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)\n5. Modulus (%)\n')

# Holds the user's selection in memory.
userInput = int(input())

# A series of if-else statements performs the proper operation that the user selects.
if userInput == 1:
    print("\nYou have selected addition.\n")
    first = int(input("Enter your first integer: "))
    second = int(input("Enter your second integer: "))
    print("\nThe addition of", first, "and", second, "is", (first + second))

elif userInput == 2:
    print("\nYou have selected subtraction.\n")
    first = int(input("Enter your first integer: "))
    second = int(input("Enter your second integer: "))
    print("\nThe subtraction of", first, "and", second, "is", (first - second))

elif userInput == 3:
    print("\nYou have selected multiplication.\n")
    first = int(input("Enter your first integer: "))
    second = int(input("Enter your second integer: "))
    print("\nThe multiplication of", first, "and", second, "is", (first * second))

elif userInput == 4:
    print("\nYou have selected division.\n")
    first = int(input("Enter your first integer: "))
    second = int(input("Enter your second integer: "))
    if second == 0:
        print("Dividing by 0 is not allowed. Exiting calculator.")
        SystemExit
    else: print("\nThe division of", first, "and", second, "is", (first / second))

elif userInput == 5:
    print("\nYou have selected modulus.\n")
    first = int(input("Enter your first integer: "))
    second = int(input("Enter your second integer: "))
    print("\nThe modulus of", first, "and", second, "is", (first % second))

# Exit prompt.
print('\nThanks for trying the Python Calculator Application!\
    \n\n*************************************************************************************\n')