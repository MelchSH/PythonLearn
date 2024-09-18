# Generators

#Seq from 1 to 9,000,000
"""
import sys

def generator(n):
    for x in range(n):
        yield x**3

values = generator(900)

for i in values:
    print(i)
print("\n")

print(sys.getsizeof(values))

"""


