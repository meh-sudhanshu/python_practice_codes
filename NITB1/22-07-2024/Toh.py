

def toh(n,src,des,aux):
    if n <= 0:
        return
    toh(n-1,src,aux,des)
    print("Move ",src," ",des)
    toh(n-1,aux,des,src)





def main():
    n = 3
    src,des,aux = 'A','C','B'
    toh(n,src,des,aux)

main()