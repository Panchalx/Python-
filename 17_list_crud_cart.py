cart=[]
inventory=["tv","Mobile","tablet","headphones","laptop","fridge","camera","videogame_console","controller","speaker"]
print("\n===== Store's Item ====")
print("1.TV\n2.Mobile\n3.Tablet\n4.Headphones\n5.Laptop\n6.fridge\n7.camera\n8.Videogame_console\n9.Controller\n10.speaker")
while True:
    print("\n==== Menu ===")
    print("1.Add to cart\n2.remove item \n3.Search Item\n4.Update Item\n5.sort Item\n6.display Item\n7.Exit")
    choice=int(input("\nEnter a Menu number:"))
    match choice:
        case 1:
            found=0
            product=input("Enter a item:").lower()
            for inventory_item in inventory:
                if inventory_item.lower() == product:
                    cart.append(product)
                    print("Item successfully added in cart")
                    found=1
                    break
                    
            if found == 0:
                print("Item not available in store")
                
        case 2:
            item_remove=input("Enter a Item name to  remove:")
            for item_list in cart:
                if item_list == item_remove:
                    cart.remove(item_list)
                    print("Item removed successfully")
                    found=1
                    break
            if found != 1:
                print("Item not found")
        case 3:
            item_search=input("Enter Item name to search:")
            for index in range(len(cart)):
                if cart[index]==item_search:
                    print("Item Founded")
                    print("Your item at:",index+1)
                    found=1
                    break
            if found!=1:
                print("Item  not found")
        case 4:
            found=0
            old_item=input("Enter a old Item to update:")
            for index in range(len(cart)):
                if cart[index]==old_item:
                    new_item=input("Enter a new item:").lower()
                    for inventory_item in inventory:
                        if inventory_item.lower() == new_item:
                            cart[index]=new_item
                            print("Item updated successfully")
                            found=1
                            break
                    if found == 0:
                        print("Item  not available in store")
                    
                    
                    
        case 5:
            cart.sort()
            print("Item place sortted  successfully")
        case 6:
            print("===== Your Cart ======")
            for item_display in cart:
                print(item_display)
        case 7:
            exit()
            break
                
                
                    