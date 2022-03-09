question=[
"how many continents are there?",
"what is the capital of india?", 
"Which course we are learning in Ng?"   
] 
options_list=[
["four","nine","seven","eight"],
["chandigarh","bhopal","chennai","delhi"],
["software engineering","councelling","tourism","agriculture"]  
]
i=0
solution=[3,4,1 ]
while i<len(question):
    print("Q",i+1,question[i]) 
    j=0
    while j<len(options_list[i]):
        print(j+1,".",options_list[i][j])
        j+=1
    user=int(input("select the option:"))
    if user== solution[i]:
        print("congrats!,your answer is correct")  
    else:
        print("sorry! your answer is wrong")    
    i=i+1