def pseudo_f(bi,xi,yi,h,g,m):
    '''
    this is a pseudo algorithm because it 
    does not divide the group into  A1,A2,A3
    randomly, instead it just determines
    the A1,A2,A3 partition based on modulo 3
    '''

    if bi % 3 == 0:
        #division A1
        return (g * bi % m, xi + 1 % m,yi)
    if bi % 3 == 1:
        #division A2
        return (bi*bi % m, 2*xi % m, 2*yi % m)
    else:
        #division A3
        return (h * bi % m, xi, yi+1 % m)
    
def pollard_rho(h,g,m):
    xi = 5
    yi = 0

    DB = dict()
    
    b = g ** xi % m

    for i in range(m ** 2):
        print("iteration ", i, xi,yi,b)
        if b in DB:
            print("past item")
            print(DB[b])
            print("new item")
            print(b,xi,yi)
            break

        DB[b] = (b,xi,yi)
        (b,xi,yi) = pseudo_f(b,xi,yi,h,g,m)

pollard_rho(11,17,311)
   
