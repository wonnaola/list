list1=[20,56,23,54,33,39,42,40]
count=0
i=0
while i<len(list1):
    if list1[i]>=20 and list1[i]<=40:
        count+=1
    i+=1
print(count)
