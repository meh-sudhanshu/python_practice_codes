arr = [1,2,3,4,5]

# print(type(arr))


from array import *


arr = array('i',[10,20,30])

# print(type(arr))
list1 = [1,2,3,45,5]
# print(list1)

list1.append('a')
# print(list1)

# list1.clear()
# print(list1)

copied_list = list1.copy()
print(copied_list)

print(list1.count('a'))
print(list1.count(122))


print(list1.pop()) # pop method will remove the last element of list
print(list1.pop())
print(list1)

print(list1.pop(0))
print(list1)



list2 = [2,2,10,23,43]
print(list2)
list2.reverse()
print(list2)


list2.sort() # sort the list in increasing order
print(list2 , "this is the list after sorting")


list2.sort(reverse = True)
print(list2)


list3 = [1,2,2,3,4,5]
list3.remove(2)
print(list3)
