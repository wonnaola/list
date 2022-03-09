list1=["1","2","3","4","5","6","7","8"]
b=[]
i=1
while i<len(list1):
    k=list1[i-1]+","+list1[i]
    b.append([k])
    i+=2
print(b)
