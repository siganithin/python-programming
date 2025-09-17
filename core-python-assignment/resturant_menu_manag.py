def add(menu, item):
    menu.append(item)
    print(f"{item} added to menu.")

def remove(menu, item):
    if item in menu:
        menu.remove(item)
        print(f"{item} removed from menu.")
    else:
        print(f"{item} not found in menu.")

def check(menu, item):
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")



initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"

add(initial_menu, add_item)
remove(initial_menu, remove_item)
check(initial_menu, check_item)

print("Updated menu:", initial_menu)
