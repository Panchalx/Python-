number=int(input("Enter a number:"))
original=number
total_power=0
while(number!=0):
    digit=number%10
    total_power=digit**3+total_power
    number=number//10
if(original == total_power):
    print("This is armstrong")
else:
    print("this is not armstrong")
print(total_power)