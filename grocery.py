def main():
    grocery_list = {}

    while True:
        try:
            item = input("").upper() #prompts for the item
            if item in grocery_list:
                    grocery_list[item] += 1
            else:
                    grocery_list[item] = 1
               
        except EOFError:
            for item, count in sorted(grocery_list.items()):
                print(f"{count} {item}")
            break
        
        except KeyError:
            pass

main()


# # Initialize an empty dictionary
# inventory = {}

# while True:
#     # Get input from the user
#     item = input("Enter an item (or 'q' to quit): ").lower()
    
#     # Check if the user wants to quit
#     if item == 'q':
#         break
    
#     # Update the inventory
#     if item in inventory:
#         inventory[item] += 1
#     else:
#         inventory[item] = 1
    
#     # Print the current inventory
#     print("\nCurrent Inventory:")
#     for item, count in inventory.items():
#         print(f"{item}: {count}")
#     print()  # Add a blank line for readability

# print("\nFinal Inventory:")
# for item, count in inventory.items():
#     print(f"{item}: {count}")