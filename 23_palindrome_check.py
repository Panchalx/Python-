try:
    value=int(input("Enter number:"))
    if value <= 0:
        print("Enter a postive number")
    else:
        reversed_value=0
        original=value
        while(value != 0):
            digit=value%10
            reversed_value=reversed_value*10+digit
            value=value//10
        if original == reversed_value:
            print("This is number palidrome")
        else:
            print("this is not palidrome")
except ValueError:
    print("enter a number")