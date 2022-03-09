list1=[6,1,3,5,6,3,1]
i=0
list2=[]
product=1
while i<len(list1):
    if list1[i] not in list2:
        list2.append (list1[i])
        product=product*list2[i]
    i+=1
print(product)

