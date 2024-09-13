import math
from functools import reduce

def gcd(a, b):
    """
    Compute the Greatest Common Divisor (GCD) of two numbers.
    """
    while b != 0:
        a, b = b, a % b
    return a

def find_divisors(n):
    """
    Find all divisors of a given number n.
    """
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def Division(*args):
    """
    Accepts multiple values and prints their common divisors.
    """
    if len(args) < 2:
        print("At least two numbers are required.")
        return
    
    # Compute the GCD of all numbers
    common_gcd = reduce(gcd, args)
    
    # Find and print the divisors of the GCD
    divisors = find_divisors(common_gcd)
    
    print(f"The common divisors of the numbers are: {divisors}")

# Example usage
Division(12, 18, 24)  # Outputs: The common divisors of the numbers are: [1, 2, 3, 6]
Division(28, 35, 42)  # Outputs: The common divisors of the numbers are: [1, 7]
