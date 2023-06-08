#left rotation
def leftRotate(arr,n):
    p=1
    while p<=n:
        temp=arr[0]
        for i in range(1,len(arr)-1):
            arr[i]=arr[i+1]
        arr[len(arr)-1]=temp
        p+=1
    return arr
#right rotation
def rightRotate(arr,n):
    p=1
    while p<=n:
        temp=arr[len(arr)-1]
        for i in range(len(arr)-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
        p+=1
    return arr
import  array
if __name__ =="__main__":
    arr=array.array('i',[1,2,3,4,5,6])
    d=2
    result=leftRotate(arr,d)
    for i in range(len(arr)):
        print(result[i],end=" ")
    print("\n")
    arr2 = array.array('i', [1, 2, 3, 4, 5, 6])
    result2=rightRotate(arr2,d)
    for i in range(len(result2)):
        print(result2[i],end=" ")
    #after righ