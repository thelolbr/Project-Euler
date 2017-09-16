"""
                Even Fibonacci numbers              
                Problem 2



Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. By starting with 
1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, find the 
sum of the even-valued terms.

                R: 4613732
"""

soma_fibo_par = 0

def fibo_par(limite):
    lista = [1]
    controle = 2

    while controle < limite:
        lista.append(controle)
        controle += lista[-2]
    
    return [x for x in lista if x % 2 == 0]

soma_fibo_par = sum(fibo_par(4000000))
print(soma_fibo_par)