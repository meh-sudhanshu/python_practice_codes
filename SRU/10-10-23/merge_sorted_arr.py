def main():
    arr1 = [-2,4,13,45,65,76,98,109]
    arr2 = [-30,-1,23,54,67,87,99,199,301]
    ans=[]
    i,j = 0,0
    while i<len(arr1) or j<len(arr2):
        if i>=len(arr1):
            while j<len(arr2):
                ans.append(arr2[j])
                j+=1
        elif j>=len(arr2):
            while i<len(arr1):
                ans.append(arr1[i])
                i+=1
        elif arr1[i]<arr2[j]:
            ans.append(arr1[i])
            i+=1
        else:
            ans.append(arr2[j])
            j+=1
    print(ans)

main()