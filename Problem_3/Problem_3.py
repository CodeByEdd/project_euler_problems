'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math


num = 600851475143
sqrt_num = math.sqrt(num)
prime_factors = []

while i <= sqrt_num:

    if sqrt_num % i == 0:
        prime_factors.append(i)
    else:
        i += 1



print(prime_factors)