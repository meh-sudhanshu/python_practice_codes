

def flipIthBit(num,i):
    mask = 1<<(i-1)
    num = num ^ mask
    return num
