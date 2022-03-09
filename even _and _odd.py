list1 = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
while i<len(list1):
    j=0
    count=0
    count1=0
    while j<len(list1):
        if list1[j]%2==0:
            count+=1  
        if list1[j]%2!=0:
            count1+=1    
        j+=1
    i+=1
print("even no.=",count)
print("odd no.=",count1)