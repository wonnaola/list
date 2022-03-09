#Write a code that works for any list, it shows the two averages as 
#the output. One is the average of even numbers and the other is the 
#average of odd numbers from the given list.

l= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
j=0
sum=0
sum1=0
avg=0
avg1=0
while i<len(l):
    if l[i]%2==0:
        sum+=l[i]
        avg=sum//4
    i+=1
print("sum of even=",sum)
print("even avg=",avg)
while j<len(l):
    if l[j]%2!=0:
        sum1+=l[j]
        avg1=sum1//7
    j+=1
print("sum of odd=",sum1)
print("avg1=",avg1)

