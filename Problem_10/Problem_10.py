'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

    while True:

        prime = calculate_if_prime(possible_prime)
        if prime is True:
            if possible_prime < 2000000:
                arr_of_primes.append(possible_prime)
                print(possible_prime)
            else:
                print(sum(arr_of_primes))
                break

        possible_prime += 1
