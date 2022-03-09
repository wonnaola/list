a=str(input("enter the number"))
b=19345
c=str(b)
i=0
while i<len(a):
    if a[i] not in c:
        print("F")
    else:
        print("T")
    i+=1