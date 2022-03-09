list1 = [10, 11, 12, 13, 14, 17, 18, 19]
sum=30
i=0
while i<len(list1):
    j=0
    while j<len(list1):
        if (list1[i]+list1[j]==sum):
            print([list1[i],list1[j]],end=" ")
        j+=1
    i+=1
        