
value=int(input("Enter a number:"))
if value < 0:
    print("please enter a postive number")
else:
    odd_count=0
    even_count=0
    original=value
    
    while(value != 0):
        num=value%10
        if(num % 2 ==0):
            even_count+=1
        else:
            odd_count+=1
        value=value//10
    print("Number : ",original)
    print("Total_odd:",odd_count)
    print("Total_even:",even_count)
