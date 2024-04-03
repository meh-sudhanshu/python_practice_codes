def main():
    m,l = map(int,input().split())
    arr = list(map(int,input().split()))
    unique_elements = set(arr)
    count = 0
    for y in unique_elements:
        for x in unique_elements:
            if x != y and abs(x - y) <= l:
                count += 1
                break  # Exit the inner loop once a match is found
    return count
print(main())