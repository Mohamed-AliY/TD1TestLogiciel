def min_int(a,b):
    if a > b :
        return b
    else :
        return a

def mediane(l):
    l = sorted(l)
    l_len = len(l)
    if l_len < 1:
        return None
    if l_len % 2 == 0 :
        print(( l[(l_len)//(2)-1] + l[(l_len)//2] ) / 2.0)
        return ( l[(l_len)//(2)-1] + l[(l_len)//2] ) / 2.0
    else:
        print(l[(l_len-1)//2])
        return l[(l_len-1)//2]



# def 