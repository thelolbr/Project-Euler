"""
                Smallest multiple               
                Problem 5 

2520 is the smallest number that can be divided 
by each of the numbers from 1 to 10 without any 
remainder.

What is the smallest positive number that is 
evenly divisible by all of the numbers from 
1 to 20?
                R: 232792560
"""

x = 2520
while sum(x % r for r in range(1,21,1)) != 0:
    x += 2520
resposta = x
print(resposta)