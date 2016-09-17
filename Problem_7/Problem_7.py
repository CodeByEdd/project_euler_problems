'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from math import sqrt

arr_of_primes = []
possible_prime = 2


def calculate_if_prime(x):

    if x == 1:
        return False
    if x == 2:
        return True
    if x == 4:
        return False

    i = 2

    while i <= sqrt(x):
        if x % i == 0:
            return False
        i += 1

    return True


if __name__ == '__main__':

    while len(arr_of_primes) < 10001:

        prime = calculate_if_prime(possible_prime)

        if prime is True:
            arr_of_primes.append(possible_prime)

        possible_prime += 1

    print(arr_of_primes[-1])
