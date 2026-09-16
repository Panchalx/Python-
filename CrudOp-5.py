animal = []


def add():
    aid = int(input("Enter Animal ID       : "))
    aname = input("Enter Animal Name     : ")
    species = input("Enter Species         : ")
    age = int(input("Enter Animal Age      : "))
    gender = input("Enter Gender          : ")
    food = input("Enter Food            : ")

    d1 = {
        "ID": aid,
        "Name": aname,
        "Species": species,
        "Age": age,
        "Gender": gender,
        "Food": food
    }

    animal.append(d1)
    print("\n*** Animal added successfully! ***")


def print_header():
    print("\n+------+----------------+----------------+------+----------+----------------+")
    print("| ID   | Name           | Species        | Age  | Gender   | Food           |")
    print("+------+----------------+----------------+------+----------+----------------+")


def print_animal(a1):
    print("| {:<4} | {:<14} | {:<14} | {:<4} | {:<8} | {:<14} |".format(
        a1["ID"],
        a1["Name"],
        a1["Species"],
        a1["Age"],
        a1["Gender"],
        a1["Food"]
    ))


def print_footer():
    print("+------+----------------+----------------+------+----------+----------------+")


def display():
    if not animal:
        print("\n*** No animals available. ***")
        return

    print("\n====================== ZOO ANIMAL COLLECTION ======================")
    print_header()

    for a1 in animal:
        print_animal(a1)

    print_footer()


def search():
    aid = int(input("Enter Animal ID to search : "))
    found = 0

    for a1 in animal:
        if a1["ID"] == aid:
            found = 1
            break

    if found == 1:
        print("\n*** Animal Found ***")
        print_header()
        print_animal(a1)
        print_footer()
    else:
        print("\n*** Animal not found. ***")


def updateName():
    aid = int(input("Enter Animal ID to update : "))
    found = 0

    for a1 in animal:
        if a1["ID"] == aid:
            found = 1
            break

    if found == 1:
        print("\n*** Animal Found ***")
        aname = input("Enter New Animal Name     : ")
        a1["Name"] = aname

        print("\n*** Animal updated successfully! ***")
        print_header()
        print_animal(a1)
        print_footer()
    else:
        print("\n*** Animal not found. ***")


def deletebyID():
    aid = int(input("Enter Animal ID to delete  : "))
    found = 0

    for a1 in animal:
        if a1["ID"] == aid:
            animal.remove(a1)
            found = 1
            break

    if found == 1:
        print("\n*** Animal deleted successfully! ***")
    else:
        print("\n*** Animal not found. ***")


def sortByAge():
    if not animal:
        print("\n*** No animals available to sort. ***")
        return

    animal.sort(key=lambda x: x["Age"])
    print("\n*** Animals sorted by age successfully! ***")
    display()
