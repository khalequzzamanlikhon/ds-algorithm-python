def ternarySearch(arr,h,l,key):
    while h>=l:
        mid1=l+(h-l)//3
        mid2=h-(h-l)//3
        if arr[mid1]==key:
            return mid1
        elif arr[mid2]==key:
            return mid2
        if arr[mid1]>key:
            h=mid1-1
            return ternarySearch(arr,h,l,key)
        elif arr[mid2]<key:
            l=mid2+1
            return ternarySearch(arr,h,l,key)
        else:
            l=mid1+1
            h=mid2-1
            return ternarySearch(arr,h,l,key)
    return -1
import  array
if __name__=="__main__":
    arr=array.array('i',[10,11,13,14,55,88])
    key=88
    l=0
    h=len(arr)-1
    result=ternarySearch(arr,h,l,key)
    if result==-1:
        print("value not found")
    else:
        print("value found at index {}".format(result))



