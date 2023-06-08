def linear_search(arr,N,x):
    for i in range(N):
        if arr[i]==x:
            return i
    return -1
if __name__ == "__main__":
    arr=[2,3,4,5,6,7]
    x=5
    N=len(arr)
    result=linear_search(arr,N,x)
    if result==-1:
        print("value is not found in the array")
    else:
        print("result is found at index {}".format(result))