
value=int(input("Enter a number:"))
if value < 0:
    print("enter a postive number")
else:
    digit_sum=0
    while(value > 0):
        digit=value%10;
        digit_sum+=digit
        value=value//10
    print("Sum of digit:",digit_sum)
