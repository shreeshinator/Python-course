name = input("Enter your name: ")
length = len(name)

print(f"Your name has {length} characters.")
name.lower()  # returns a lowercase version of the name
name.upper()  # returns an uppercase version of the name
print("Does your name start with 'A'?", name.startswith("A"))  # checks if the name starts with "A"
print("Does your name end with 'n'?", name.endswith("n"))  # checks if the name ends with "n"
index = name.find("a")  # returns the index of the first occurrence of "a" in the name, or -1 if not found
if index != -1:
    print(f"The index of 'a' in your name is: {index}")
else:
    print("The letter 'a' is not found in your name.")

