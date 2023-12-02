def get_number_of_set_bits(n):
    count = 0
    while n > 0:
        if n%2 == 1:
            count+=1
            n = n>>1
        else:
            n = n>>1
    return count

def main():
    print(get_number_of_set_bits(15))
main()