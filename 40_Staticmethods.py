# Static methods are methods that belong to a class rather than an instance of the class. They can be called on the class itself without needing to create an instance. Static methods are defined using the @staticmethod decorator and do not have access to the instance (self) or class (cls) variables. They are often used for utility functions that perform a task related to the class but do not require access to instance or class data.

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

print(Employee.is_valid_position("Rocket Scientist"))