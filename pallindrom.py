name=[ 'n', 'i', 't', 'i', 'n' ]
i=1
a=[]
while i<=len(name):
    a.append(name[-i])
    i+=1
print(a)
if name==a:
    print("palindrome")
else:
    print("not palindrome")