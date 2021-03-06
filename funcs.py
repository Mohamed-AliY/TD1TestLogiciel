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
        # print(( l[(l_len)//(2)-1] + l[(l_len)//2] ) / 2.0)
        return ( l[(l_len)//(2)-1] + l[(l_len)//2] ) / 2.0
    else:
        # print(l[(l_len-1)//2])
        return l[(l_len-1)//2]

def moyenne(l):
    somme = sum(l)
    nb_elements = len(l)
    moyenne = somme / nb_elements
    # print("moyenne ",moyenne)
    # print("nb_elements ",nb_elements)
    # print("somme",somme)
    return moyenne

def ecart_type(l):
    moy=moyenne(l)
    s=0
    for e in l:
        s+=pow(e-moy,2)
    s/=len(l)
    return pow(s,0.5)

def estGeo(l):
    if len(l)<1:
        return None
    r=l[1]/l[0]
    for i in range(1,len(l)-1):
        if l[i+1]!=r*l[i]:
            return False
    return True

def estArith(l):
    if len(l)<1:
        return None
    r=l[1]-l[0]
    for i in range(1,len(l)-1):
        if l[i+1]!=r+l[i]:
            return False
    return True

def suiteGeo(n,l):
    verif=None
    l2=[]
    if estGeo(l):
        r=l[1]/l[0]
        suiv=r*l[len(l)-1]
        for i in range(n):
            l2.append(suiv)
            suiv=suiv*r
    return verif,l2
def suiteArith(n,l):
    verif=None
    l2=[]
    if estArith(l):
        r=l[1]-l[0]
        suiv=r+l[len(l)-1]
        for i in range(n):
            l2.append(suiv)
            suiv=suiv+r
    return verif,l2
# def 