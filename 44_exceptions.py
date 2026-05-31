# exceptions are errors that occur during the execution of a program. They can be handled using try-except blocks to prevent the program from crashing.
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ValueError:
    print("That's not a valid number. Please enter an integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")