marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
while i<len(marks):
    j=0
    total=0
    while j<len(marks[i]):
        total+=marks[i][j]
        average=(total)//len(marks[i])
        j+=1
    print(total)
    print("average=",average)
    i+=1