values=[4,5,1,2,34,6,7,8,45,32,]
largest=values[0]
smallest=values[0]
second_largest=values[0]
second_smallest=values[0]
for value in values:
    if largest < value:
        second_largest=largest
        largest=value
    elif value > second_largest and value != largest:
        second_largest=value
for value in values:
    if smallest > value:
        second_smallest=smallest
        smallest=value
    elif value < second_smallest or value == smallest:
        second_smallest=value
        
print(second_largest)
print(second_smallest)
