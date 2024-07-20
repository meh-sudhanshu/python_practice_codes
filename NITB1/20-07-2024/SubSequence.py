
def printAllSubsequence(arr,index,ans):
    if len(arr) == index:
        print(ans)
        return
    printAllSubsequence(arr,index+1,ans)
    printAllSubsequence(arr,index+1,ans+[arr[index]])


def main():
    arr = [1,2,3]
    printAllSubsequence(arr,0,[])
main()