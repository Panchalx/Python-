number=int(input("Enter a number:"))
original=number
reversed_value=0
while(number!=0):
    digit=number%10
    reversed_value=reversed_value*10+digit
    number=number//10
if(original == reversed_value):
    print("This is palidrome")
else:
    print("this is not palidrom")
print(reversed_value)