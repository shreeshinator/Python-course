class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
    def drive(self):
        print(f"The {self.make} {self.model} is driving.")
    def stop(self):
        print(f"The {self.make} {self.model} has stopped.")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car1.display_info()  # Output: 2020 Toyota Camry
car1.drive()  # Output: The Toyota Camry is driving.
car1.stop()  # Output: The Toyota Camry has stopped.
car2.display_info()  # Output: 2019 Honda Civic
car2.drive()  # Output: The Honda Civic is driving.
car2.stop()  # Output: The Honda Civic has stopped.