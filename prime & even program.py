# PRIME AND EVEN NUMBER
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_even(number):
    return number % 2 == 0

# Input
num = int(input("Enter a number: "))

# Checking if prime or even
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

if is_even(num):
    print(num, "is an even number.")
else:
    print(num, "is not an even number.")


