items=[6,3,2,6,7,8,92,]
index=0
while(index<len(items)):
    scan=index+1
    while(scan < len(items)):
        if items[scan] == items[index]:
           items.pop(scan) 
        else:
            scan+=1        
        scan+=1
    index+=1
print(items)
 