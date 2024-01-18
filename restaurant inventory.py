def get_inventory():
    items = int(input("Enter the amount of items to be added to the inventory: "))
    initial_inventory = {
         'apple': 10,
         'banana': 20,
         'dates': 30,
         'milk': 50
    }
    
    dict_inventory = initial_inventory.copy()
    for i in range(items):
        item_name = input(f"Enter item [{i+1}] name: ")
        item_quant = int(input("Enter the quantity of the item: "))
        dict_inventory[item_name] = item_quant
    print("||| THESE ARE THE INVENTORY ITEMS |||")
    for i, (key, value) in enumerate(dict_inventory.items(), 1):
        print(f"{i}. {key} {value}")
    
    return dict_inventory

def get_dishes():
    dish = int(input("Enter the amount of dishes needed to be added to the list: "))
    initial_dishes = {
        "Rose Milk": {'milk': 2, 'rose': 2},
        "Banana Milk": {'milk': 2, 'banana': 4}
    }
    
    dict_dish = initial_dishes.copy()
    for i in range(dish):
        dish_name = input(f"Enter the dish [{i+1}] name: ")
        dict_dish[dish_name] = {}

        ingredients = int(input(f"List the amount of ingredients needed for {dish_name}: "))

        for j in range(ingredients):
            ingredient_name = input("Enter the ingredients name: ")
            ingredient_quant = int(input("Enter the quantity of ingredients: "))
            dict_dish[dish_name][ingredient_name] = ingredient_quant
    return dict_dish

def get_order(dict_dish, dict_inventory):
   
    print("||| THESE ARE THE MENU ITEMS |||")
    for i, key in enumerate(dict_dish.keys(), 1):
        print(f"{i}. {key}")
    
    order_choose = int(input("How many food items do you want to order: "))
    order_nums = []

    for k in range(order_choose):
        order_opts = int(input(f"Enter item number {k + 1}: "))
        order_nums.append(order_opts)

    for f in order_nums: #order_nums is a list of selected items from the menu
        dish_name = list(dict_dish.keys())[order_nums - 1] #here we area getting the dish name by using order_nums number
        ingredients_needed = dict_dish[dish_name]

        for ingredient, quantity in ingredients_needed.items():
            if ingredient in initial_inventory and initial_inventory[ingredient] >= quantity:
                initial_inventory[ingredient] -= quantity
            else:
                print(f"Not enough {ingredient} in the inventory for {dish_name}")

    print("Updated Inventory:")
    for i, (key, value) in enumerate(initial_inventory.items(), 1):
        print(f"{i}. {key}: {value}")

def show_inventory(dict_inventory):
    print("||| CURRENT INVENTORY |||")
    for i, (key, value) in enumerate(dict_inventory.items(), 1):
        print(f"{i}. {key}: {value}")

def main():

    dict_inventory = {}
    initial_dishes = {}

    while True:
        print("\nMENU:")
        print("1. Update Inventory")
        print("2. Update Dishes")
        print("3. Select Menu")
        print("4. Show Inventory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            dict_inventory = get_inventory()
        elif choice == '2':
            initial_dishes = get_dishes()
        elif choice == '3':
            get_order(initial_dishes, initial_inventory)
        elif choice == '4':
            show_inventory(initial_inventory)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
