MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

onOff = True

while onOff:
    choice = input("choose coffee (esspresso, latte, cappuccino) ? ")

    if choice == "off" :
        onOff = False
    elif choice == "report":
        print(f"water : {resources['water']}ml")
        print(f"mile : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}ml")

    
