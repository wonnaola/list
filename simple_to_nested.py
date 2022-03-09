list=[[1,2,3],[4,5,6],[7],[8,9]]
b=[]
i=0
while i<len(list):
    if type(list[i])==type([]):
        j=0
        while j<len(list[i]):
            b.append(list[i][j])
            j+=1
    else:
        b.append(list[i])
    i+=1
print(b)

