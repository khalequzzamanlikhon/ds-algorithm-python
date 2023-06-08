import array
arr=array.array('i',[1,2,3,4,5])
print(arr.index(2))
#printing using loops
for i in range(len(arr)):
    print(arr[i],end=" ")
print("\n")
arr.reverse()
for i in range(len(arr)):
    print(arr[i],end=" ")
