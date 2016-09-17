'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

a = 1
b = 2
c = 3

# Square


def square(x):
    return x * x


# Check if a^2 + b^2 = c^2


def check_pythagorean_triplet(a, b):
    if square(a) + square(b) == square(c):
        print("A: " + str(a) + " B: " + str(b) + " C: " + str(c))
        print("The product of a, b, and c is: " + str(a * b * c))


while a <= 1000:

    if a + b + c == 1000:
        check_pythagorean_triplet(a, b)
        break

    b = a + 1

    while b <= 1000:

        if a + b + c == 1000:
            check_pythagorean_triplet(a, b)
            break

        c = b + 1

        while c <= 1000:

            if a + b + c == 1000:
                check_pythagorean_triplet(a, b)
                break

            c += 1

        b += 1

    a += 1
