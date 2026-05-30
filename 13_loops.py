name = input("Enter your name: ")

while name == "":
    print("Name cannot be empty. Please enter your name.")
    name = input("Enter your name: ")

print(f"Hello, {name}!")

number = int(input("Enter a number between 1 and 10: "))
while number < 1 or number > 10:
    print("Invalid input. Please enter a number between 1 and 10.")
    number = int(input("Enter a number between 1 and 10: "))

print(f"You entered: {number}")