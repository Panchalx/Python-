values=[22,43,56,42,34]

largest=values[0]
for value in values:
    if value > largest:
        largest=value
    
print("Maximum number:",largest)
smallest=values[0]
for value in values:
    if value < smallest:
        smallest=value

print("Minimum number:",smallest)