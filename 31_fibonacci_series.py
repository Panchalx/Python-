terms=int(input("Enter a number:"))
current=0
next_value=1
for _ in range(terms):
    print(current)
    following=current+next_value
    current=next_value
    next_value=following
    