# This program demonstrates the use of try and except blocks to handle exceptions.
try:
    n = int(input("Enter a number: "))
    reult = 10 / n
    print("Result is: ", reult)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")

#string to Int converter
try:
    s = int(input("Enter number: "))
    print("Square: ", s * s)
except ValueError:
    print("Invalid Input") 