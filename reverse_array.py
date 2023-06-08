def reverseArray(arr):
    start=0
    end=len(arr)-1
    while start<end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1
    return arr


if __name__=="__main__":
    arr=[1,2,3,4,5,6]
    print("before reverse : \n")
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print("\n")
    result=reverseArray(arr)
    print("\nafter reverse the array is :\n")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print("\n")

