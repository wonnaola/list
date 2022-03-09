q=["what is the capital of india?"]
s=["1.Chandigarh","2.Bhopal","3.Chennai","4.Delhi"]
solution=[4]
i=0
while i<len(q):
    print("Q.",q) 
    j=0
    while j<len(s):
        print(s[j])
        j+=1
    sol=int(input("enter the number:"))
    if sol==solution[i]:
        print("congratulations!correct answer")
    else:
        print("better luck next time")
    i+=1
    print()