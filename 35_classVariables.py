#class variables are defined within a class but outside of any instance methods. They are shared among all instances of the class, meaning that if you change the value of a class variable, it will affect all instances that reference that variable.
class car:
    wheels = 4  # This is a class variable
    num_of_cars = 0  # This is a class variable

    def __init__(self, make, model):
        self.make = make  # This is an instance variable
        self.model = model  # This is an instance variable
        car.num_of_cars += 1  # Increment the class variable when a new car is created

car1 = car("Toyota", "Camry")
car2 = car("Honda", "Civic")
print(car1.make)  # Output: Toyota
print(car2.model)  # Output: Civic
print(car.wheels)  # Output: 4
print(car.num_of_cars)  # Output: 2 because we created two car instances