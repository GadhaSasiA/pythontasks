class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0  

    def describe(self):
        return f"{self.year} {self.make} {self.model}"

    def drive(self, miles):
        self.odometer += miles
        print(f"You've driven {miles} miles. Total on odometer: {self.odometer}")

my_car = Car("Toyota", "Corolla", 2020)

print(my_car.describe())

my_car.drive(100)


class Car:
    def __init__(self, make, model, year):
        self._make = make  # "Private" attribute
        self._model = model
        self._year = year
    
    def display_info(self):
        print(f"{self._year} {self._make} {self._model}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        # Use 'super' to call the parent class's initializer
        super().__init__(make, model, year)
        self.battery_size = battery_size  # New attribute

    def display_info(self):
        # Override the method to add extra information
        super().display_info()  # Call parent class method
        print(f"Battery Size: {self.battery_size} kWh")
# Create an ElectricCar object
e_car = ElectricCar("Tesla", "Model 3", 2021, 75)
e_car.display_info()


#encapsulation
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Encapsulated attribute
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            return "Insufficient funds"
        self._balance -= amount
        return self._balance

# Create a bank account object
account = BankAccount(1000)

# Encapsulation protects direct access to _balance
print(account.get_balance())  # Output: 1000
account.deposit(500)
print(account.get_balance())  # Output: 1500


#inheritence
# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some generic sound"

# Derived class
class Dog(Animal):
    def speak(self):
        return "Bark"

# Derived class
class Cat(Animal):
    def speak(self):
        return "Meow"

# Create instances of derived classes
dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Bark
print(cat.speak())  # Output: Meow


#polimorphism
def animal_sound(animal):
    # Polymorphism: Calls the appropriate 'speak' method
    return animal.speak()

# Test with different animal types
print(animal_sound(dog))  # Output: Bark
print(animal_sound(cat))  # Output: Meow
