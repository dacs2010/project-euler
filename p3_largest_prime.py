'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''


def prime_finder():
    n = 600851475143
    i = 2
    
    while n >= i:
        if n % i == 0 and n != i:
            n = n // i
            i = 2
        else:
            i += 1

    print(f'{n} largest prime... i think')


prime_finder()
