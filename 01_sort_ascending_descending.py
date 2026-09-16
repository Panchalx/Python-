values=[4,2,7,6,8,3,9,1]
index=0
while(index < len(values)):
    scan=index+1
    while(scan < len(values)):
        if values[scan] < values[index]:
            hold=values[scan]
            values[scan]=values[index]
            values[index]=hold
        scan+=1
    index+=1
            
print("Acending order:-",values)
index=0
while(index < len(values)):
    scan=index+1
    while(scan < len(values)):
        if values[scan] > values[index]:
            hold=values[scan]
            values[scan]=values[index]
            values[index]=hold
        scan+=1
    index+=1
print("Decending order:-",values)