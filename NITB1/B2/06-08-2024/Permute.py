

def permute(arr):
    if len(arr) == 1:
        return [arr]
    ans = []

    for i in range(len(arr)):
        fixedElement = arr[i]
        subSequence = arr[0:i]+arr[i+1:]
        allPermutation = permute(subSequence)
        for per in allPermutation:
            per.append(fixedElement)
            ans.append(per)

    return ans




def main():
    arr = [1,2,3]
    ans = permute(arr)
    print(ans)

main()