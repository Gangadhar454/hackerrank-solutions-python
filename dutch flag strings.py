def dutch_flag_strings(arr):
    low=0
    mid=0
    high=len(arr)-1
    while(mid<=high):
        x=arr[mid]
        if(x=="R"):
            arr[mid],arr[low]=arr[low],arr[mid]
            mid=mid+1
            low=low+1
        elif(x=="G"):
            mid=mid+1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high=high-1
    return arr
print(dutch_flag_strings(["G","G","R","B","R","B","B","G","R","B","R"]))
