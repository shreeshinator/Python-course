def describe_pet(name, animal_type="dog", color="brown"):
    """Return a description of a pet using default and keyword arguments."""
    return f"My {color} {animal_type} is named {name}."


def total_price(price, quantity=1, discount=0):
    """Return the total price after applying a discount."""
    return price * quantity * (1 - discount)


# Example usage with default arguments:
print(describe_pet("Buddy"))
print(describe_pet("Whiskers", animal_type="cat"))
print(describe_pet("Goldie", animal_type="fish", color="gold"))

# Example usage with keyword arguments:
print(total_price(price=20, quantity=3))
print(total_price(price=20, quantity=3, discount=0.1))
print(total_price(quantity=2, price=15, discount=0.2))
