# #yoyoyoy
# yo = ("eat a sandwich")

# print (yo)

def main():                 #dictionary of fruits with calories
        fruit_calories = {
            "apple": 130,
            "avocado": 50,
            "banana": 110,
            "cantaloupe": 50,
            "grapefruit": 60,
            "grapes": 90,
            "honeydew melon": 50,
            "kiwifruit": 90,
            "lemon": 15,
            "lime": 20,
            "nectarine": 60,
            "orange": 80,
            "peach": 60,
            "pear": 100,
            "pineapple": 50,
            "plums": 70,
            "strawberries": 50,
            "sweet cherries": 100,
            "tangerine": 50,
            "watermelon": 80
        }
        fruit = input("Item: ").lower() #prompts for the fruit
        if fruit in fruit_calories:
              print("Calories: " + str(fruit_calories[fruit])) #outputs the calories
        else:
              print()


main()