def is_divisible(n):
    i=1
    while(i<n) :
        if n%i==0 and i>1:
            return True
        i=i+1
    return False

def is_prime(p):
    s=''
    for i in range(2,p+1):
        if (is_divisible(i))!=True:
            s=s+str(i)+' '
    
    return s 
        
        
print(is_prime(50))
