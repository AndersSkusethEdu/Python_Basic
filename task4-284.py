
import random

def generate_random_numbers():
    return [random.randint(1, 50) for i in range(10)]

def substitute(numbers):
    for i in range(10):
        if numbers[i] % 5 == 0:
            numbers[i] = numbers[i] ** 2

    return numbers


random_numbers = generate_random_numbers()
substituted = substitute(random_numbers.copy())

print("\nBefore substitution, the list is:", random_numbers)
print("After substitution, the list is:", substituted, "\n")
