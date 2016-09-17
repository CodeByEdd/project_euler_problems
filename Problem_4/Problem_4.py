'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

x = 101
palindrome_list = []

while x <= 999:

    y = 101

    while y <= 999:

        temp_ans = x * y

        if str(temp_ans) == str(temp_ans)[::-1]:
            palindrome_list.append(temp_ans)

        y += 1
        
    x += 1

print(palindrome_list)
