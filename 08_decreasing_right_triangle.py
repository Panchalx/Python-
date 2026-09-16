
size=int(input("Enter a number:"))
if size < 0:
    print("Enter a postive number")
else:
    for row in range(size , 0,-1):
        for col in range(row,0,-1):
            print("*",end=" ")
        print(" ")
