def zeros_to_end(arr):
    count=0
    for i in range(len(arr)):
        if (arr[i]!=0):
            arr[i],arr[count]=arr[count],arr[i]
            count+=1
    return arr
arr=[1,2,3,4,0,0,6,7]
print(zeros_to_end(arr))
