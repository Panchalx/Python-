for row in range(1,6):
    for  _ in range(5-row):
        print(" ",end=" ")
    for value in range(5,5-row,-1):
        print(value,end=" ")
    print()