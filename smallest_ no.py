#write a python program to get the smallest number from the list.

list1=[56,7,35,27,78,12]
i=0
smallest=list1[0]
while i< len(list1):
    if list1[i]<smallest:
        smallest=list1[i]
    i+=1
print(smallest)