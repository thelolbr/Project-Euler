"""
                10001st prime               
                Problem 7 


By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?

                R: 104743
100"""

import time

descobrir = 10001
primos = [2]
n = 3
tempo = time.time()
while len(primos) < descobrir:
    eh_primo = True
    for i in primos:
        # print(i)
        if n % i == 0:
            eh_primo = False
            break
    if eh_primo:
        primos.append(n)
    n += 2
print('O %sº primo é o %s.' % (descobrir, primos[-1]))
print('Tempo de execução: %2f' % (time.time() - tempo))