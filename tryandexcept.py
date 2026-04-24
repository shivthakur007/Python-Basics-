try:
    n = int(input("Enter a number: "))
    reult = 10 / n
    print("Result is: ", reult)
except ZeroDivisionError:
    print("You cannot divide by zero.")