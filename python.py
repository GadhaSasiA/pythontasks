def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Test the function
string1 = "listen"
string2 = "silent"
print(f"Are '{string1}' and '{string2}' anagrams? {are_anagrams(string1, string2)}")


def find_largest(lst):
    return max(lst)

# Test the function
numbers = [1, 2, 3, 4, 5]
print(f"The largest element in the list {numbers} is {find_largest(numbers)}")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Test the function
start_range = 10
end_range = 50
print(f"Prime numbers between {start_range} and {end_range} are: {prime_numbers_in_range(start_range, end_range)}")


def remove_duplicates(lst):
    return list(set(lst))

# Test the function
numbers = [1, 2, 2, 3, 4, 4, 5]
print(f"Original list: {numbers}")
print(f"List after removing duplicates: {remove_duplicates(numbers)}")


def find_second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

# Test the function
numbers = [1, 2, 3, 4, 5]
print(f"The second largest element in the list {numbers} is {find_second_largest(numbers)}")


def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

# Test the function
list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(f"Merged and sorted list: {merge_sorted_lists(list1, list2)}")



def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Test the function
input_str = "Hello, World!"
print(f"The number of vowels in the string '{input_str}' is {count_vowels(input_str)}")


def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Test the function
number = 121
print(f"Is the number {number} a palindrome? {is_palindrome(number)}")
