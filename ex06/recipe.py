#! /usr/bin/env python3

cookbook = {}

def add_recep():
    ingredients = []
    tmp = ""
    name = input("Enter a name:\n")
    print("Enter ingredience")
    while (True):
        tmp = input()
        if (tmp == ""):
            break
        ingredients.append(tmp)
    meal = input("Enter a meal type:\n")
    prep_time= input("Enter a preparation time:\n")

    cookbook[name] = {
    'ingredients': ingredients,
    'meal': meal,
    'prep_time': prep_time,
}

def print_res():
    user = input("Please enter a recipe name to get it's details: ")
    if (user in cookbook):
        recipe = cookbook[user]
        print(f"Recipie for {user}")
        print(f"Ingredients list: {recipe['ingredients']}")
        print(recipe["meal"])
        print(recipe["prep_time"])
    else:
        print("Sorry, but there's no such a recipe")
        
        return
def print_book():
    if (not cookbook):
        print("Cookbook is empty")
    else:
        for name, recipe in cookbook.items():
            print(f"\nRecipe: {name}")
            print(f"   Ingredients: {recipe['ingredients']}")
            print(f"   Meal: {recipe['meal']}")
            print(f"   Prep time: {recipe['prep_time']}")
def remove_res():
    user = input("Which recipe do you want to delete?: ")
    if (not cookbook):
        print("Sorry, but there's no such a recipe")
    else:
        cookbook.pop(user)
def show_menu():
    print("\nWelcome to the Python cookbook! \nList of available options: ")
    print("  1: Add a recipe\n  2: Delete a recipe\n  3: Print recipe\n  4: Print the cookbook\n  5: Quit\n\n")

def main():
    show_menu()
    while (True):
        user = ""
        user = input("Please select  option: ")
        if (user == "1"):
            add_recep()
        elif (user == "2"):
            remove_res()
        elif (user == "3"):
            print_res()
        elif (user == "4"):
           print_book()
        elif (user == "5"):
            print("\nCookbook closed. Goodbye !")
            break
        else:
            print("Sorry, this option doesn't exist")
            show_menu()
        
main()
    


    