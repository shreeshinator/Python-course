def greet(name, greeting="Hello"):
    """Return a greeting message for the given name."""
    return f"{greeting}, {name}!"


def add_numbers(a, b=5):
    """Return the sum of two numbers, with a default second value."""
    return a + b


# Example usage:
print(greet("Shreesh"))
print(greet("Shreesh", greeting="Welcome"))

print(add_numbers(3))
print(add_numbers(3, 7))
