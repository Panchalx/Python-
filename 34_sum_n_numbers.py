
limit=int(input("Enter a number:"))
counter=1
total_sum=0
if(limit < 0):
    print("please Enter a postive number")
else:
    for counter in range(counter,limit+counter):
        total_sum+=counter
        
print("Total:",total_sum)
        
