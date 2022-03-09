list1=[1,2,2,5,8,4,4,8]
i=0
b=[]
count=0
while i<len(list1):
    if list1[i] not in b:
        b.append (list1[i])
        count+=1
    i+=1
print(count)