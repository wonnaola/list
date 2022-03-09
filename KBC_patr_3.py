question=[
"How many continents are there?",
"What is the capital of india?",
"W hich course are we learning in NG?"    
]
options_list=[
["Four","Nine","Seven","Eight"],
["Chandigarh","Bhopal","Chennai","Delhi"],
["Software engineering","Counseling","Tourism","Agriculture"]
]
i=0
while i<len(question):
    print("Q",i+1,question[i])
    j=0
    while j<=len(options_list):
        print(options_list[i][j])
        j=j+1
    i=i+1