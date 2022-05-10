import math
from math import factorial

def Newton():
    n = int(input())
    k = int(input())


    n_fact = math.factorial(n)
    k_fact = math.factorial(k)
    nk_fact = math.factorial(n-k)

    newt_pattern = n_fact/k_fact*nk_fact
    print(newt_pattern)


Newton()
