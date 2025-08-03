#! /usr/bin/env python3

cookbook = {
    'ingredients': [],
    'meal': "",
    'prep_time': 0,
    'name': "",

}

def add_recep():
    ingredients = []
    tmp = ""
    cookbook['name'] = input("Enter a name:\n")
    print("Enter ingredience")
    while (True):
        tmp = input()
        if (tmp == ""):
            break
        ingredients.append(tmp)
    cookbook["ingredients"] = ingredients
    cookbook['meal'] = input("Enter a meal type:\n")
    cookbook['prep_time'] = input("Enter a preparation time:\n")
add_recep()
    


    