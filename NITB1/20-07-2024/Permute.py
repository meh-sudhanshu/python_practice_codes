def permute(arr):
    if len(arr) == 1:
        return [arr]
    ans = []
    for i in range(len(arr)):
        fixedEle = arr[i]
        subSequence = arr[:i]+arr[i+1:]
        allPermutation = permute(subSequence)
        for per in allPermutation:
            per.append(fixedEle)
            ans.append(per)
    return ans

def main():
    arr = [1,2,3,4]
    ans = permute(arr)
    print(ans)
main()