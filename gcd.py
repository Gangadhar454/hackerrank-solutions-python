def gcd(i,j):
    gcd=1
    
    for x in range(1,i+1):
        
        if (i%x==0) and (j%x==0):
            
            if(x>gcd):
                
                gcd=x
    return gcd
print(gcd(24,36))
           
    
