'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number
would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

from math import sqrt

triangle_numbers_list = [1, 3, 6]
divisors_count = 0
i = 1

while divisors_count < 500:
    temp_value = triangle_numbers_list[-1]
    while i <= sqrt(temp_value):
        if temp_value / i != type(float):
            divisors_count += 1
            if divisors_count == 500:
                print("Answer: " + str(temp_value))
                break
        i += 1
    triangle_numbers_list = triangle_numbers_list.append(sum(triangle_numbers_list))