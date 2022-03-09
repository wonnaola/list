list1=[1,7,5,4,8,7,1,5]
i=0
k=[]
while i<len(list1):
    if list1[i] not in k:
        k.append(list1[i])
    i+=1
print(k)
    
