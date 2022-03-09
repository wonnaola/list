#write a python program to get the largest number from the list.

list1=[76,56,10,23,67,29]
i=0
largest=list1[0]
while i< len(list1):
    if list1[i]>largest:
        largest=list1[i]
    i+=1
print(largest)

