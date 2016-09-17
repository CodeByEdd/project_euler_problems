'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


from math import sqrt

num = 600851475143
i = 2

while i < sqrt(num):
    while num % i == 0:
        num = num / i
    i += 1

print(int(num))