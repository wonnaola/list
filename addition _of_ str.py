list1=["1","2","3","4","5","6","7","8"]
i=0
k=[]
while i<len(list1):
    j=list1[i]+list1[i+1]
    k.append(j)
    i+=2
print(k)
