# arr = [0]*10
# print(arr)


# # len --- used to find the length of array
# print(len(arr),"length of array")

# # append --> use to insert a value at the end of the array
# arr.append(10)
# print(arr," 10 appended to the array")

# removedValue = arr.pop()
# print(removedValue, "gets popped")
# print(arr)
# removedValue = arr.pop(5)
# print(removedValue, " gets popped")
# print(arr)

# arr = [100]+arr
# print(arr , '100 got appended')

# def printArray(arr):
#     for row in arr:
#         for ele in row:
#             print(ele,end = " ")
#         print()


# arr1 = [[0 for i in range(4)] for j in range(5)]
# #printArray(arr1)
# arr1[1][2] = 100
#printArray(arr1)


# arr2 = [[0]*5]*4
# printArray(arr2)
# arr2[2][1] = 100
# print()
# print()
# print()
# print("-------------updated array------------------")
# printArray(arr2)


arr = [[i for i in range(5)] for j in range(4)]

for i in range(5):
    for j in range(4):
        print(arr[j][i],end=" ")





