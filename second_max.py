# write a python program to bring out the second maximum.
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=0
scondmax=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    elif numbers[i]>scondmax and scondmax<max:
        scondmax=numbers[i]
    i+=1
print(scondmax)
    