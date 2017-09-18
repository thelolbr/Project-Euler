"""
                Sum square difference               
                Problem 6 

The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 
3025 − 385 = 2640.

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.

                R: 25164150
"""



def diff_soma_potencia(limite):
    contador_soma = 0
    contador_pot = 0
    for x in range(1,limite + 1):
        contador_soma += x
        contador_pot += x**2
    return (contador_soma ** 2) - contador_pot
print(diff_soma_potencia(100))