import CrudOp as c1


while True:
    print("\n")
    print("============================================================")
    print("                 ZOO MANAGEMENT SYSTEM")
    print("============================================================")
    print("  1. Add Animal")
    print("  2. Display Animals")
    print("  3. Update Animal Name")
    print("  4. Delete Animal")
    print("  5. Search Animal")
    print("  6. Exit")
    print("------------------------------------------------------------")

    choice = input("  Enter your choice (1-6) : ")
    print("------------------------------------------------------------")

    if choice == "1":
        c1.add()

    elif choice == "2":
        c1.display()

    elif choice == "3":
        c1.updateName()

    elif choice == "4":
        c1.deletebyID()

    elif choice == "5":
        c1.search()

    elif choice == "6":
        print("\n============================================================")
        print("       Thank you for using Zoo Management System!")
        print("============================================================")
        break

    else:
        print("\n*** Invalid choice! Please enter a number from 1 to 6. ***")
