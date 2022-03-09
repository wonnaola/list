binary_num=[1,0,0,1,1,0,1,1]
i=-1
power=0
sum=0
while i>=-(len(binary_num)):
    k=binary_num[i]*2**power
    sum=sum+k
    power+=1
    i=i-1
print(sum)