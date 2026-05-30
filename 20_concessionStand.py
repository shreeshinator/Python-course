#python concession stand program
print("Welcome to the Concession Stand!")
menu = {
    "Popcorn": 100,
    "Soda": 30,
    "Candy": 25,
    "Hot Dog": 200
}   
total = 0
cart = []
print("--------------------Menu--------------------")
for key, price in menu.items():
    print(f"{key:<10}: ₹{price:.2f}")
print("--------------------------------------------")
while True:
    item = input("Enter the item you want to buy (or 'q' to finish): ").strip()
    if item.lower() == "q":
        break
    # normalize input to match menu keys (case-insensitive)
    key = item.title()
    if key in menu:
        cart.append(key)
        print(f"{key} added to cart.")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")

for item in cart:
    total = total + menu.get(item, 0)
print("--------------------Receipt--------------------")
for item in cart:
    print(f"{item:<10}: ₹{menu[item]:.2f}")
print(f"Your total is: ₹{total:.2f}")


