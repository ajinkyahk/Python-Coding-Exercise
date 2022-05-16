n=6
f1=-1
f2=1
l1 = []
for i in range(n+1):  
    sum= f1 + f2
    l1.append(sum)
    f1=f2
    f2=sum
    

print(l1)
