#These are the marks of any student for the last three years.
#You have to calculate total marks for all the three years.

marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# i=0
# j=0
# k=0
# sum1=0
# sum2=0
# sum3=0
# while i<len(marks[0]):
#     sum1=sum1+marks[0][i]
#     i+=1
# while j<len(marks[1]):
#     sum2=sum2+marks[1][j]
#     j+=1
# while k<len(marks[2]):
#     sum3=sum3+marks[2][k]
#     k+=1
# print(sum1)
# print(sum2)
# print(sum3)
# print("total marks ","=",sum1+sum2+sum3)

i=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum+=marks[i][j]
        j+=1
    i+=1
print(sum)
 
