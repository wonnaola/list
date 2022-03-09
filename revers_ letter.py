places=["delhi",' ,', "gujrat", ', ',"rajasthan",',' ,"punjab",' ,' ,"kerala"]
# places.reverse()
# print(places)

# b=[]
# i=-1
# while i>=-len(places):
#     b.append(places[i])
#     i-=1
# print(b)

temp=" "
length=len(places)-1
while length>=0:
    temp=temp+places[length]
    length=length-1
print(temp)