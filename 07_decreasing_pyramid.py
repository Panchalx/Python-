
size=int(input("Enter a number:"))
if size < 0:
    print("Enter a postive number")
else:
    for row in range(size,0,-1):
        for space in range(size-row):
            print("  ",end="")
        for star in range(1,row*2):
            print("*",end=" ")
        print()

