def get_hashed_value(value):
    return value%10

def get_next_available_index(hash_table,current_index):
    for i in range(current_index,len(hash_table)):
        if hash_table[i] == 0:
            return i
        elif i == len(hash_table)-1:
            i = 0




def main():
    search_key = [12,32,45,34,65,78,90,112]
    n = 10
    hash_table = [0 for i in range(n)]

    for key in search_key:
        current_index = get_hashed_value(key)
        if hash_table[current_index] == 0:
            hash_table[current_index] = key
        else:
            next_index = get_next_available_index(hash_table,current_index)
            hash_table[next_index] = key

    print(hash_table)

main()