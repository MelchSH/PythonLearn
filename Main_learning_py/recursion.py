
n = 7

fact = 1
"""
# Non-Recursive
while n > 0:
    fact = fact * n
    n  -= 1

print(fact)
"""

# Recursion version
def factorial(n):
    if n < 1:
        return 1
    else:
        number = n*factorial(n-1)
        return number

print(factorial(n))

