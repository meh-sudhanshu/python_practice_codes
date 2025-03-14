


def isPowerOf2(num):
    ans = num & (num-1)
    if ans == 0:
        return True
    return False



def main():
    num = 9
    ans = isPowerOf2(num)
    print(ans)
main()