a=["Wonnao","Shimray"]
i=0
c=""
while i<len(a):
    j=0
    while j<len(a[i]):
        if j==0:
            m=a[i][j].upper()
            c=c+"."+m
        j=j+1
    i=i+1
print(c[1:])
