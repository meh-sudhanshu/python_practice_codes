def hash_fn(value):
    return value%10

def probe(hash_table,ci):
    probe_number = 1
    while hash_table[ci] != -1:
        ci = ci + probe_number**2
        if ci >= len(hash_table):
            ci = ci%10
        if hash_table[ci] == -1:
            return ci
        else:
            probe_number+=1
def quadratic_probing(search_keys,n):
    hash_table = [-1 for i in range(n)]
    for key in search_keys:
        ci = hash_fn(key)
        if hash_table[ci] == -1:
            hash_table[ci] = key
        else:
            ni = probe(hash_table,ci)
            hash_table[ni] = key
    return hash_table


def main():
    search_keys = [34,54,65,78,32,98]
    n = 10
    hash_table = quadratic_probing(search_keys,n)
    print(hash_table)


main()