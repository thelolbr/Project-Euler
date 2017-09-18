"""
                Summation of primes
                Problem 10 


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

                R: 
"""

import time

descobrir = 2000000
primos = [2]
n = 3
verifica = 0
tempo = time.time()
while verifica < descobrir:
    eh_primo = True
    for i in primos:
        # print(i)
        if n % i == 0:
            eh_primo = False
            break
    if eh_primo:
        primos.append(n)
        verifica = i
    n += 2
print(sum(primos))
print('Tempo de execução: %2f' % (time.time() - tempo))