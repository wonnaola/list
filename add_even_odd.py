#Write a code that works for any list, it should give two sums as outputs,
# one is the sum of odd numbers present in the list and the other is the sum of 
# even numbers present in the list.

num = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
j=0
sum=0
sum1=0
while i<len(num):
    if num[i]%2==0:
        sum+=num[i]
    i+=1
print("even=",sum)
while j<len(num):
    if num[j]%2!=0:
        sum1+=num[j]
    j+=1
print("odd=",sum1)