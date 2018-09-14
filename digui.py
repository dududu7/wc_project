# python
# -*- coding: 


def factorial(n):
    if n == 0 or n == 1:
        return 1
    total = 1
    for i in range(2, n + 1):
        total *= i
    print('%d'%(total))
    return total



    if word[0] == '':
        Length = 0
    else: