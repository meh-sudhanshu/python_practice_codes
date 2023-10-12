

def find_number_of_ways(n):
    if n==1:
        return 1
    if n<=0:
        return 0
    return find_number_of_ways(n-1)+find_number_of_ways(n-2)+find_number_of_ways(n-3)

print(find_number_of_ways(5))