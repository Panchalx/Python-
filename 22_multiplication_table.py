
value =int(input("Enter a number:"))
if(value <= 0):
    print("Enter a postive number")
else:
    multiplier=1
    while(multiplier<=10):
        print(f"{value}*{multiplier}={value*multiplier}")
        multiplier+=1