"""
                Largest prime factor                
                Problem 3 


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

                R: 6857
"""

def max_factor(num):
    """Find the maximum prime factor."""
    factor = 2
    while factor * factor <= num:
        while num % factor == 0:
            num /= factor
        factor += 1
    if (num > 1):
        return num
    return factor
print(int(max_factor(600851475143)))