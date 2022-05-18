import math
from math import factorial

input = list(input())
n = int(input[0])
k = int(input[-1])



def Newton(n,k):

    n_fact = math.factorial(n)
    k_fact = math.factorial(k)
    nk_fact = math.factorial((n-k))

    newt_pattern = int(n_fact/(k_fact*nk_fact))
    print(newt_pattern)


Newton(n,k)
