# Day8_Primes.py

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_n_primes(n):
    count = 0
    number = 2
    
    while count < n:
        if is_prime(number):
            print(number, end=" ")
            count += 1
        number += 1

# Input
n = int(input("Enter value of N: "))
print_n_primes(n)