a=[[1,4],[5,2],[7,6],[8,1]]
d=[]
i=0
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum+=a[i][j]
        j+=1
    d.append(sum)
    i+=1
print(d)