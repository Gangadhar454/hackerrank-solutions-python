def dutch(arr):
    l=len(arr)-1
    low=0
    mid=0
    while(mid<=l):
        x=arr[mid]
        if(x==0):
            arr[mid],arr[low]=arr[low],arr[mid]
            mid=mid+1
            low=low+1
        elif(x==1):
            mid=mid+1
        else:
            arr[mid],arr[l]=arr[l],arr[mid]
            l=l-1
    return arr
l=[0,1,2,1,2,0]
print(dutch(l))
