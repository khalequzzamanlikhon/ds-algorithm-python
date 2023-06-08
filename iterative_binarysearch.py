import  array
def binarySearch(arr,key):
    l=0
    r=len(arr)-1
    while l<=r:
        m=l+(r-l)//2
        if arr[m]==key:
            return m
        else:
            if arr[m]<key:
                l=m+1
            else:
                r=m-1
    return -1

if __name__ =="__main__":
    arr=array.array('i', [2, 3, 4, 10, 40,55])
    x=60
    result=binarySearch(arr,x)
    if result==-1:
        print("value not found in the array")
    else:
        print("value is found at index {}".format(result))

