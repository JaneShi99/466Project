'''
m denotes the prime p, z/pz
o denotes the order of the group
'''

def pseudo_f(bi,xi,yi,h,g,m):
    '''
    this is a pseudo algorithm because it 
    does not divide the group into  A1,A2,A3
    randomly, instead it just determines
    the A1,A2,A3 partition based on modulo 3
    '''

    o = m-1 # order
    if bi % 3 == 0:
        #division A1
        return (g * bi % m, xi + 1 % o,yi)
    if bi % 3 == 1:
        #division A2
        return (bi*bi % m, 2*xi % o, 2*yi % o)
    else:
        #division A3
        return (h * bi % m, xi, yi+1 % o)
    
def pollard_rho(h,g,m):
    xi = 6
    yi = 0

    DB = dict()
    
    b = g ** xi % m

    for i in range(m ** 2):
        print('iteration ', i,' b=', b,' xi=',xi,' yi=',yi)
        if b in DB:
            print("collision detected!")
            print("past item")
            print(DB[b])
            print("new item")
            print(b,xi,yi)
            break

        DB[b] = (b,xi,yi)
        (b,xi,yi) = pseudo_f(b,xi,yi,h,g,m)

pollard_rho(11,17,311)
   
