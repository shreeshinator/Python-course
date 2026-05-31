# decorators are functions that modify the behavior of other functions. They are often used to add functionality to existing code without modifying it directly.
 # *args and **kwargs allow the wrapper function to accept any number of positional and keyword arguments, which are then passed to the original function (func) when it is called. Without *args and **kwargs, the wrapper would not be able to handle functions with different signatures, making it less flexible and potentially causing errors when the decorated function is called with arguments.
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles...")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs): 
        print("Adding fudge...")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here's your {flavor} ice cream!")

get_ice_cream("chocolate")