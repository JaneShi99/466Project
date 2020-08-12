import math

'''
The first two algorithms are found at:
https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

They are included for the purpose of finding modulo inverse.
'''


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def baby_list(h,g,m):
    g_inv = modinv(g,m)
    for x in range(int(math.sqrt(m)+1)):
        print  (h*g_inv ** x)%m, '&',

    print('')

def giant_list(h,g,m):
    n = int(math.sqrt(m)+1)
    for x in range(n):
        print(g ** (x*n))%m, '&',
    print('')

baby_list(11,17,311)
giant_list(11,17,311)


