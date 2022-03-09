# write a python program to count the number of the strings where the 
# string length is 2 or more and the first and the last character are 
# same from a given string list.
list1=['abc','xyz','aba','1221']
i=0
count=0
while i< len(list1):
    if len(list1[i])>1 and list1[i][0]==list1[i][-1]:
        # print("the given words are :",i)
        count+=1
    i+=1
print(count)



