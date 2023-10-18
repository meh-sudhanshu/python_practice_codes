
def hash_function(value):
    return value%10
def main():
    search_keys = [12,23,45,43,42,54,53,65,75,67,87]
    n = 11
    hash_table = [[] for i in range(n)]
    for value in search_keys:
        hash_value = hash_function(value)
        hash_table[hash_value].append(value)
    print(hash_table)
main()
