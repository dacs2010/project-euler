'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def find_mult():
    x = range(1, 1000)
    num_list = []

    for i in x:
        if i % 3 == 0:  
            num_list.append(i)
        elif i % 5 == 0:
            num_list.append(i)
    print(sum(num_list))

find_mult()