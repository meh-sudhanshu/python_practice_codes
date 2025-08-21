


def main():
    arr = [1,7,3,6]
    for i in range(1,len(arr)+1):
        j = 0
        k = i-1
        while k < len(arr):
            print(arr[j:k+1])
            j+=1
            k+=1
main()