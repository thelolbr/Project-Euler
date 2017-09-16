"""
                Largest palindrome product              
                Problem 4 


A palindromic number reads the same both ways. The largest 
palindrome made from the product of two 2-digit numbers 
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

                R: 906609
"""

x = 0
y = 0
pol = 0
while x <= 999:
    y = x
    while y <= 999:
        temp = str(x * y)
        tempInverso = temp[::-1]
        if temp == tempInverso:
            polTemp = int(temp)
            if polTemp > pol:
                pol = polTemp
        y += 1
    x += 1
print(pol)