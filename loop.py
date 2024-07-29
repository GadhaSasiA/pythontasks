numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

count = 1

while count <= 5:
    print(count)
    count +=1

for number in numbers:
    if number == 3:
        break
    print(number)


# Example: Skipping the rest of the loop iteration when a condition is met
for number in numbers:
    if number == 3:
        continue
    print(number)


# Example: Nested loop to print a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j}", end=" ")
    print()

def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)

