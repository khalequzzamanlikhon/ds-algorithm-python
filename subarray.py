def subArray(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            for k in range(i,j):
                print(arr[k],end=" ")
            print("\n")

if __name__=="__main__":
    arr=[1,2,3,4,5,6]
    subArray(arr)
