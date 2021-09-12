def countways(n):
    if(n==1 or n==0):
        return 1
    if (n==2):
        return 2
    return countways(n-1)+countways(n-2)+countways(n-3)
print(countways(4))


