List = eval(input("Enter a List"))
Dict = {}
for a in range(0,len(List)):
    count=0
    if List[a] not in Dict:
        for b in range(0,len(List)):
            if(List[a]==List[b]):
                count+=1
        Dict[List[a]]=count
for b in Dict:
    print("Count of",b,"is : ",Dict[b])
