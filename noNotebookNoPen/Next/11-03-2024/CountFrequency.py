arr = [1,1,1,2,2,3,1,0,0,4,2,3,2]
low = 0
high = 5
f_arr = [0 for i in range(high+1)] 
for i in range(len(arr)):
    ele = arr[i]
    f_arr[ele]+=1
for i in range(len(f_arr)):
    if f_arr[i] != 0:
        print(str(i)+" has occured"+str(f_arr[i])+" times")