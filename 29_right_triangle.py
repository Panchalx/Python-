
size=int(input("Enter a number:"))
if size < 0:
    print("Enter a postive number")
else:
    for row in range(1,size+1):
        for col in range(1,row+1):
            print("*",end=" ")
        print(" ")


