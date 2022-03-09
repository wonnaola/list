l= "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
substr = "over"
rep="on"
str=l.split()
i=0
while i<len(str):
    if str[i]==substr:
        del str[i]
    else:
        print(str[i],end=" ")
    i+=1
a=l.replace (substr,rep)
print(a)
    

