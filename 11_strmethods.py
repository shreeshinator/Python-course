name = input("Enter your name: ")
length = len(name)

print(f"Your name has {length} characters.")

index = name.find("a")  # returns the index of the first occurrence of "a" in the name, or -1 if not found
if index != -1:
    print(f"The index of 'a' in your name is: {index}")
else:
    print("The letter 'a' is not found in your name.")

