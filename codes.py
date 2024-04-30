count = 0
while count < 5:
    print(count)
    count += 1


x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is less than 10")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name}."

alice = Person("Alice", 30)
print(alice.greet())


my_list = [1, 2, 3, "hello"]
my_list.append(4)  # Adds an item
my_list[0] = "new"  # Modifies an item
print(my_list)
