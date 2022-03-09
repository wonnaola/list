list1=[20,10,25,5]
i=1
b=[]
while i<len(list1):
    sub=list1[i-1]-list1[i]
    i+=2
    b.append(sub)
print(b)
