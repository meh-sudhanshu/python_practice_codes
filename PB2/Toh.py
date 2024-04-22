def toh(n,src,des,aux):
    if n == 1:
        print(src,"->",des)
        return
    toh(n-1,src,aux,des)
    print(src,"->",des)
    toh(n-1,aux,des,src)


toh(3,"A","C","B")