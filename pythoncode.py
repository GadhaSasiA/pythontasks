# Basic arithmetic operations
a = 10
b = 5

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")




my_list = [1, 2, 3, 4, 5]

print(f"First element: {my_list[0]}")

my_list.append(6)
print(f"List after appending: {my_list}")

my_list.remove(3)
print(f"List after removing 3: {my_list}")

print(f"First three elements: {my_list[:3]}")


# Working with dictionaries
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

print(f"Name: {my_dict['name']}")

# Adding a new key-value pair
my_dict['job'] = 'Engineer'
print(f"Dictionary after adding job: {my_dict}")

# Removing a key-value pair
del my_dict['age']
print(f"Dictionary after removing age: {my_dict}")

# Iterating over a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
