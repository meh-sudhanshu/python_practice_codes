
# [1] --> [[1]]
def permute(arr):
    if len(arr) == 1:
        return [arr]
    ans = []
    for i in range(len(arr)): 
        fixedElement = [arr[i]]
        subArray = arr[0:i]+arr[i+1:]
        allPermutation = permute(subArray)
        for permutation in allPermutation:
            ans.append(fixedElement+permutation)

    return ans




def main():
    arr = [1,2,3]
    ans = permute(arr)
    print(ans)

main()


