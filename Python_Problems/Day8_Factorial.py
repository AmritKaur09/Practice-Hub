# Day8_Factorial.py

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Input
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not defined for negative numbers")
else:
    print("Factorial:", factorial(num))