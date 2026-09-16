def prime_flag(value):
    prime_flag=True
    for divisor in range(2,value):
        if(value % divisor == 0):
            prime_flag=False
            break
        
    if prime_flag == True:
        return True
    else:
        return False
    
value=int(input("Enter  a number:"))
if prime_flag(value) == True:
    print("this is prime number")
else:
    print("this is not prime number")
        
        