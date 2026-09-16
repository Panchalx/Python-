
first=int(input("Enter a number 1:"))
second=int(input("Enter a number 2:"))
third=int(input("Enter a number 3:"))
if first>second and first>third:
    print(f"{first} is large")
elif second>first and second>third:
    print(f"{second} is large")
else:
    print(f"{third} is large")
