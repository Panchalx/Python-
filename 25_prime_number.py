number=int(input("Enter a number:"))
if(number<=1):
    print("This is not prime number")
else:
    prime_flag=True
    for divisor in range(2,number):
        if(number%divisor==0):
            prime_flag=False
            break

if prime_flag==True:
    print("This is prime number")
else:
    print("This is not prime number")
    