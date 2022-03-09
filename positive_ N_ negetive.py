l=[2,3,-4,6,7,2,-8,]
i=0
# count1=0
# count2=0
sum=0
sum1=0
while i<len(l):
    if l[i]>0:
        # count1+=1
        sum+=l[i]
    if l[i]<0:
        # count2+=1
        sum1+=l[i]
    i+=1
# print("positive",count1)
# print("negetive",count2)
print("positive=",sum)
print("negetive=",sum1)
    