my_map = {}
# putting a key value pair
my_map["key"] = "This is a value"
my_map[0] = "ZERO"
my_map[1.3] = "ONE.THREE"
my_map[0] = "UPDATED ZERO"

for key in my_map:
    print(my_map[key],end=" ")



#Printing and defaulting if a key does not exist
# print(my_map)
# try:
#     print(my_map[10])
# except:
#     print("key does not exists")
# print(my_map[1.3])


#del my_map[0]
# print(my_map)


# if "key" in my_map:
#     print("key key is present")
# else:
#     print("key 0 is not present")