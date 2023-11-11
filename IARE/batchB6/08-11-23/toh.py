def toh(n,src,des,aux):
    if n <= 0:
        return
    toh(n-1,src,aux,des)
    print("move",src,"->",des)
    toh(n-1,aux,des,src)


src,des,aux = 'A','C','B'
n = 3
toh(n,src,des,aux)