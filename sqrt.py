def sqroot(x):
    if (x==0 or x==1):
        return x
    else:
        start=1
        end=x
        while(start <=end):
            mid=(start+end)//2
            if(mid*mid == x):
                return mid
            elif(mid*mid < x):
                start=mid+1
                ans=mid
            else:
                end=mid-1
    return ans
print(sqroot(9))

