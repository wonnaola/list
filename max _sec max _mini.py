list1=[8,5,9,5,4,7,10]
max=list1[0]
sec_max=list1[0]
third_max=list1[0]
i=0
while i<len(list1):
    if list1[i]>max:
        max=list1[i]
    i+=1
i=0
while i<len(list1):
    if list1[i]>sec_max and list1[i]!=max:
        sec_max=list1[i]
    i+=1
while i<len(list1):
    if list1[i]>third_max and list1[i]!=max and list1[i]!=sec_max:
        third_max=list1[i]
    i+=1
print(max)
print(sec_max)
print(third_max)
       

      



    
