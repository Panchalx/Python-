
first=int(input("Enter a number:"))
second=int(input("Enter a number 2:"))
print(f"Before \n A={first}\n B={second}")
temporary=first
first=second
second=temporary
print(f"After \n A={first}\n B={second}")