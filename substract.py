list1=[1,3,2]
i=1
b=[]
while i<len(list1):
    sub=list1[i]-list1[0]
    b.append(sub)
    i+=1
print(b)
