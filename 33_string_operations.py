text = input("Enter a string: ")
print("1.find length\n2.string in uppercase\n3.string in lowercase\n4.string with initial capital\n5.split the string\n6.Exit")

while True:
    menu_choice = int(input("Enter a choice: "))
    match menu_choice:
        case 1:
            print(len(text))
            
        case 2:
            print(text.upper())

        case 3:
            print(text.lower())
            
        case 4:
            print(text.capitalize())
            
        case 5:
            print(text.split())
            
        case 6:
            exit()
            break
