list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
list2=[]
while i<len(list1):
    sub=list1[i]-i
    list2.append(sub)
    i+=1
print(list2)