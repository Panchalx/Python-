
value =int(input("Enter a number:"))
if value <=0:
    print("please enter a postive number")
else:
    factorial=1
    counter=1
    for counter in range(counter,value+counter):
        factorial=factorial*counter
        counter+=1
    print("Factrioal:",factorial)
